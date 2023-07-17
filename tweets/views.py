from rest_framework import viewsets

from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action

from .renderers import DefaultRenderer

from .serializers import PostSerializer, UserSerializer, CommentSerializer
from tweets.models import Post, User, Comment

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

import re
from rest_framework.views import APIView

class EmojiCountView(APIView):
    renderer_classes = (DefaultRenderer,)
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        post_id = request.data.get('post_id')
        if post_id:
            try:
                post = Post.objects.get(id=post_id)
                emoji_count = count_emojis(post.content)
                return Response({'emoji_count': emoji_count, 'post_content': post.content})
            except Post.DoesNotExist:
                return Response({'ErrorDetail': 'Post not found'}, status=404)
        return Response({'ErrorDetail': 'Invalid request'}, status=400)


def count_emojis(text):
    emoji_regex = r'[\U0001F300-\U0001F5FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U00002600-\U000026FF\U00002700-\U000027BF\U0000FE00-\U0000FE0F\U0001F900-\U0001F9FF\U0001F1E6-\U0001F1FF]'
    emojis = re.findall(emoji_regex, text)
    emoji_count = len(emojis)
    return emoji_count

class WordWithMoreThan5CharsCountView(APIView):
    renderer_classes = (DefaultRenderer,)
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        post_id = request.data.get('post_id')
        if post_id:
            try:
                post = Post.objects.get(id=post_id)
                words_with_more_than_5_chars = count_words_with_more_than_5_chars(post.content)
                return Response({'words_with_5_chars_or_more': words_with_more_than_5_chars, 'post_content': post.content})
            except Post.DoesNotExist:
                return Response({'ErrorDetail': 'Post not found'}, status=404)
        return Response({'ErrorDetail': 'Invalid request'}, status=400)

def count_words_with_more_than_5_chars(post_content):
    words = post_content.split()
    count = sum(1 for word in words if len(word) > 5)
    return count

class SentimentCountView(APIView):
    renderer_classes = (DefaultRenderer,)
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        post_id = request.data.get('post_id')
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({'ErrorDetail': 'Post not found'}, status=404)
        
        total, sentiment_counts = count_sentiment_words(post.content)
        
        response_data = {
            'post': post.content,
            'total_sentiments': total,
            'sentiment_counts': sentiment_counts
        }
        
        return Response(response_data)

def count_sentiment_words(post_content):
    sentiment_words = {
        'enojo': ['enojo', 'rabia', 'frustración', 'frustrado'],
        'alegría': ['alegría', 'alegre', 'felicidad', 'entusiasmo'],
        'duda': ['miedo', 'incertidumbre', 'preocupación', 'inseguridad']
    }
    
    words = post_content.split()
    count = 0
    sentiment_counts = {sentiment: 0 for sentiment in sentiment_words}
    
    for word in words:
        cleaned_word = remove_special_chars(word.lower())  # Aplicar limpieza a cada palabra
        for sentiment, sentiment_word_list in sentiment_words.items():
            if cleaned_word in sentiment_word_list:
                if sentiment_counts[sentiment] == 0:
                    count += 1
                sentiment_counts[sentiment] += 1
    
    return count, sentiment_counts

def remove_special_chars(word):
    # Remover caracteres especiales utilizando expresiones regulares
    cleaned_word = re.sub(r'[^\w\s]', '', word)
    return cleaned_word

class LoginViewSet(viewsets.ViewSet):
    renderer_classes = (DefaultRenderer,)
    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return Response({'ErrorDetail': 'Invalid credentials'}, status=401)
        
        # Authentication successful
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({'access_token': access_token})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = (DefaultRenderer,)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    renderer_classes = (DefaultRenderer,)
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    renderer_classes = (DefaultRenderer,)
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]





