from rest_framework import serializers
from social.models import Post,Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['id', 'body','author','created_on']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.ReadOnlyField(source='post.author.username')
    class Meta:
        model = Comment
        fields = ['id','comment','author','post','created_on']
