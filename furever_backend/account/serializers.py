from rest_framework import serializers
from .models import User, FriendshipRequest, ShelterProfile, Pet, Event

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'friends_count', 'posts_count', 'get_avatar',)

class FriendshipRequestSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = FriendshipRequest
        fields = ('id', 'created_by',)

class ShelterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShelterProfile
        fields = ('workers', 'animals')

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['name', 'age', 'breed', 'type', 'gender', 'color', 'birthplace', 'spayed', 'personality', 'image']

    def create(self, validated_data):
        return Pet.objects.create(**validated_data)
    
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'date', 'time', 'location')
