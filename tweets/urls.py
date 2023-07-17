from django.urls import path, include
from rest_framework import routers
from tweets import views

from .views import LoginViewSet, EmojiCountView, WordWithMoreThan5CharsCountView, SentimentCountView

router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'comment', views.CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginViewSet.as_view({'post': 'login'}), name='login'),
    path('signup/', views.UserViewSet.as_view({'post': 'create'})),
    path('emoji-post-count/', EmojiCountView.as_view(), name='emoji-count'),
    path('word-post-count/', WordWithMoreThan5CharsCountView.as_view(), name='emoji-count'),
    path('word-sentiment-post-count/', SentimentCountView.as_view(), name='emoji-count'),
]
