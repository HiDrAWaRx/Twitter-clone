from django.http import HttpResponse


def home(request):
    return HttpResponse("Home page " + str(request.user))
