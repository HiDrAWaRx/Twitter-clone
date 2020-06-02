from django.urls import path

from .views import (
    add_tweet,
    add_comment,

    home,
    post_view,
    user_view)

urlpatterns = [
    path('post/add/', add_tweet, name='add_tweet'),
    path('comment/add/', add_comment, name='add_comment'),
    path('', home, name='home_view'),
    path('tweet/<pk>/', post_view, name='post_view'),
    path('user/<user>/', user_view, name='user_view'),
]
