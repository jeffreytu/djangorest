from django.http import JsonResponse
from django.shortcuts import render

# third-party imports
from rest_framework.response import Response
from rest_framework.views import APIView

class TestView(APIView):
    #get request endpoint
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'jeff',
            'age': 32
        }
        return Response(data)

# Create your views here.
# def test_view(request):
#     data = {
#         'name': 'jeff',
#         'age': 32
#     }
#     return JsonResponse(data)