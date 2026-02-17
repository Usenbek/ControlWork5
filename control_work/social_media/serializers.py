from rest_framework import serializers
from .models import Post, Comment


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = 'author title body created_at'.split()

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = 'author post body created_at'.split()
    
class CommentDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = '__all__'

class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta: 
        model = Post
        fields = '__all__'
        