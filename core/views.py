from django.http import JsonResponse
from django.shortcuts import render

# third-party imports
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView #wrapper provided by the REST api framework
from rest_framework import generics

from .serializers import PostSerializer #check if post is valid serialization
#post request will receive data and need to make sure format matches the serializers - like forms
from .models import Post


# Create your views here.
# def test_view(request):
#     data = {
#         'name': 'jeff',
#         'age': 32
#     }
#     return JsonResponse(data)


# class TestView(APIView):

#     permission_classes = [IsAuthenticated, ]

#     #get request method endpoint
#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         #when passing in data keyword, we want to check that this is valid
#         serializer = PostSerializer(data=request.data)
#         #wont be able to save the serializer if it's not valid
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

class PostView(mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    #mixins are containers of functionality
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()