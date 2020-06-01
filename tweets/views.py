# def home(request):
#     return HttpResponse("Home page " + str(request.user))
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.shortcuts import render

from tweets.models import UserProfile


def home(request):
    context = {
        "user": request.user,
        "user_avatar": UserProfile.objects.get(user=request.user).avatar
    }
    return render(request, 'feed/home.html', context)


@receiver(user_signed_up)
def add_UserProfile(user, **kwargs):
    profile = UserProfile(user=user)
    profile.save()
