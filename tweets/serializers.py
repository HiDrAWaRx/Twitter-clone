from rest_framework import serializers
from .models import Post,  Comment, User

from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'password', 'first_name', 'last_name', 'email', 'is_active']

    def to_representation(self, obj):
        ret = super().to_representation(obj)
        ret.pop('password')

        return ret 
    
    def create(self, validated_data):
        user = User(**validated_data)
        try:
            user.full_clean()
            user.save()
        except ValidationError as e:
            raise serializers.ValidationError(str(e))

        return user
    

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField (
        slug_field='username',
        queryset=User.objects.all(),
    )

    def create(self, validated_data):
        author_username = validated_data.pop('author')
        try:
            author = User.objects.get(username=author_username)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid author username", 427)
        post = Post(**validated_data)
        post.author = author
        post.save()
        return post

    class Meta:
        model=Post
        fields=['author', 'id', 'content', 'add_date']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )
    
    post = serializers.SlugRelatedField(
        slug_field="content",
        queryset=Post.objects.all(),
    )

    def create(self, validated_data):
        author_username = validated_data.pop('author')
        post_content = validated_data.pop('post')
        try:
            author = User.objects.get(username=author_username)
            post = Post.objects.get(content=post_content)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid author username", 457)
        except Post.DoesNotExist:
            raise serializers.ValidationError("Post not found.", 459)

        comment = Comment(**validated_data)
        comment.author = author
        comment.post = post
        comment.save()
        return comment
    
    class Meta:
        model=Comment
        fields=['content', 'author', 'post', 'add_date']