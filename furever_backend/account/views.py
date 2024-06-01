from django.http import HttpResponse
from django.shortcuts import render

from .models import User




def activateemail(request):
    email = request.GET.get('email', '')
    id = request.GET.get('id', '')

    if email and id:
        user = User.objects.get(id=id, email=email)
        user.is_active = True
        user.save()
    
        return HttpResponse('🎉 Pawsome News! You are Activated! <br><br> Woohoo! Your account is now activated and ready to roll. 🐾✨ You can go ahead and log in to join the fun with all your furry friends. Let the adventures begin! <br><br> Ready, set, go! 🚀')
    else:
        return HttpResponse('The parameters is not valid!')
    
