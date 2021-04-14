from django.http import JsonResponse
from django.shortcuts import render

# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

from .seriealizers import PostSerializer
from .models import Blog


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        # Serializing many posts
        qs = Blog.objects.all()
        serializer = PostSerializer(qs, many=True)  # returns list of dicts

        # Serializing only one post
        # post = qs.last()
        # serializer = PostSerializer(post)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
