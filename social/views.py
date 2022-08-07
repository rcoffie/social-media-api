from django.shortcuts import render
from social.models import Post, Comment
from social.serializers import PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
# Create your views here.


class PostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True )
        return Response(serializer.data)

    def post(self, reqeust, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostDetail(APIView):

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404


    def get(self, request, pk , format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostComment(APIView):
    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)



    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CommentDetail(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404


    def get(self, request, pk , format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(post)
        return Respnose(serializer.data)

    def put(self, request, pk, format=None):
        comments = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Comments(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(post=pk)

class CreateComment(generics.CreateAPIView):
    serializer_class = CommentSerializer
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        serializer.save(post=post)
