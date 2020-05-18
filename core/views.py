from django.http import JsonResponse
from django.shortcuts import render

# third-party imports
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer #check if post is valid serialization
#post request will receive data and need to make sure format matches the serializers - like forms
from .models import Post

class TestView(APIView):
    #get request endpoint
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        #when passing in data keyword, we want to check that this is valid
        serializer = PostSerializer(data=request.data)
        #wont be able to save the serializer if it's not valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
       

# Create your views here.
# def test_view(request):
#     data = {
#         'name': 'jeff',
#         'age': 32
#     }
#     return JsonResponse(data)