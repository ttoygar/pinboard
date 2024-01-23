from rest_framework import serializers
from posts.models import Thread, Post


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ['id', 'title', 'created_at', 'creator']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'thread', 'message', 'created_at', 'author']