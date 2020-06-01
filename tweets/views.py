# def home(request):
#     return HttpResponse("Home page " + str(request.user))
from django.shortcuts import render


def home(request):
    return render(request, 'feed/home.html', {})
