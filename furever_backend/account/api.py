from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from notification.utils import create_notification

from rest_framework.response import Response
from rest_framework import status

from .forms import SignupForm, ProfileForm, ShelterProfileForm
from .models import User, FriendshipRequest, ShelterProfile, Pet, Event
from .serializers import UserSerializer, FriendshipRequestSerializer, PetSerializer, ShelterProfileSerializer, EventSerializer

@api_view(['GET'])
def me(request):
    if request.user.is_authenticated:
        return JsonResponse({
            'id': request.user.id,
            'name': request.user.name,
            'email': request.user.email,
            'avatar': request.user.get_avatar()
        })
    else:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        user = form.save()
        user.is_active = False
        user.save()

        url = f'{settings.WEBSITE_URL}/activateemail/?email={user.email}&id={user.id}'

        send_mail(
            "Please verify your email",
            f"The url for activating your account is: {url}",
            "noreply@wey.com",
            [user.email],
            fail_silently=False,
        )
    else:
        message = form.errors.as_json()
    
    print(message)

    return JsonResponse({'message': message}, safe=False)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_pet(request):
    data = request.data.get('pet', request.data)
    message = 'success'

    pet_serializer = PetSerializer(data=data)

    if pet_serializer.is_valid():
        pet = pet_serializer.save()
        message = {'message': 'Pet created successfully', 'pet': pet_serializer.data}
    else:
        message = {'message': 'Pet creation failed', 'pet_errors': pet_serializer.errors}
    
    print(message)  # Logging the message for debugging purposes

    return JsonResponse(message, safe=False, status=201 if pet_serializer.is_valid() else 400)

@api_view(['POST'])
def list_pet(request): 
    pets = Pet.objects.all()
    serializer = PetSerializer(pets, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_shelter_profile(request):
    shelter_profile_data = request.data.get('shelter_profile')
    shelter_profile_serializer = ShelterProfileSerializer(data=shelter_profile_data)

    if shelter_profile_serializer.is_valid():
        shelter_profile = shelter_profile_serializer.save()
        return JsonResponse({'message': 'Shelter profile created successfully', 'shelter_profile': shelter_profile_serializer.data}, status=201)
    else:
        return JsonResponse({'message': 'Shelter profile creation failed', 'shelter_profile_errors': shelter_profile_serializer.errors}, status=400)

@api_view(['POST'])
def create_event(request):
    event_data = request.data.get('event')
    event_serializer = EventSerializer(data=event_data)

    if event_serializer.is_valid():
        event = event_serializer.save()
        return JsonResponse({'message': 'Event created successfully', 'event': event_serializer.data}, status=201)
    else:
        return JsonResponse({'message': 'Event creation failed', 'event_errors': event_serializer.errors}, status=400)

@api_view(['GET'])
def friends(request, pk):
    user = User.objects.get(pk=pk)
    requests = []

    if user == request.user:
        requests = FriendshipRequest.objects.filter(created_for=request.user, status=FriendshipRequest.SENT)
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = requests.data

    friends = user.friends.all()

    return JsonResponse({
        'user': UserSerializer(user).data,
        'friends': UserSerializer(friends, many=True).data,
        'requests': requests
    }, safe=False)


@api_view(['GET'])
def my_friendship_suggestions(request):
    serializer = UserSerializer(request.user.people_you_may_know.all(), many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def send_friendship_request(request, pk):
    user = User.objects.get(pk=pk)

    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(created_by=user)
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(created_by=request.user)

    if not check1 or not check2:
        friendrequest = FriendshipRequest.objects.create(created_for=user, created_by=request.user)

        notification = create_notification(request, 'new_friendrequest', friendrequest_id=friendrequest.id)

        return JsonResponse({'message': 'friendship request created'})
    else:
        return JsonResponse({'message': 'request already sent'})

@api_view(['POST'])
def editprofile(request):
    user = request.user
    email = request.data.get('email')

    if User.objects.exclude(id=user.id).filter(email=email).exists():
        return JsonResponse({'message': 'email already exists'})
    else:
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
        
        serializer = UserSerializer(user)

        return JsonResponse({'message': 'information updated', 'user': serializer.data})
    

@api_view(['POST'])
def editpassword(request):
    user = request.user
    
    form = PasswordChangeForm(data=request.POST, user=user)

    if form.is_valid():
        form.save()

        return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'message': form.errors.as_json()}, safe=False)


@api_view(['POST'])
def handle_request(request, pk, status):
    user = User.objects.get(pk=pk)
    friendship_request = FriendshipRequest.objects.filter(created_for=request.user).get(created_by=user)
    friendship_request.status = status
    friendship_request.save()

    user.friends.add(request.user)
    user.friends_count = user.friends_count + 1
    user.save()

    request_user = request.user
    request_user.friends_count = request_user.friends_count + 1
    request_user.save()

    notification = create_notification(request, 'accepted_friendrequest', friendrequest_id=friendship_request.id)

    return JsonResponse({'message': 'friendship request updated'})