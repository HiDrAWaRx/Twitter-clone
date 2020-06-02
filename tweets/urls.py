from django.urls import path, include
from .views import home,add_tweet, post_view, add_comment
urlpatterns = [
    path('', home, name='home_view'),
    path('post/add/', add_tweet, name='add_tweet'),
    path('comment/add/', add_comment, name='add_comment'),
    path('<user>/<pk>/', post_view, name='post_view'),
]
