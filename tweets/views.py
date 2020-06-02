# def home(request):
#     return HttpResponse("Home page " + str(request.user))
from allauth.account.signals import user_signed_up
from django.core.paginator import Paginator
from django.dispatch import receiver
from django.shortcuts import render, redirect

from tweets.models import UserProfile, Post, Comment


def home(request):
    tweets = Post.objects.all().order_by("-add_date")

    paginator = Paginator(tweets, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "user": request.user,
        "user_avatar": UserProfile.objects.get(user=request.user).avatar,
        "tweets": page_obj,
    }
    return render(request, 'feed/home.html', context)


def add_tweet(request):
    tweet = Post(content=request.POST.get('content'), author=request.user)
    tweet.save()
    return redirect('home_view')


def add_comment(request):
    pk = request.POST.get('id_post')
    comment = Comment(content=request.POST.get('content'), author=request.user, post=Post.objects.get(pk=pk))
    comment.save()
    return redirect('post_view', user=request.user, pk=pk)


def post_view(request, user, pk):
    context = {
        "user": request.user,
        "user_avatar": UserProfile.objects.get(user=request.user).avatar,
        "tweet": Post.objects.get(pk=pk),
        "pk": pk,
    }
    return render(request, 'feed/post.html', context)


@receiver(user_signed_up)
def add_UserProfile(user, **kwargs):
    profile = UserProfile(user=user)
    profile.save()
