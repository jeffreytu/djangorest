from rest_framework import serializers
#Serialization is the process of turning an object in memory into a stream of
#bytes so you can do stuff like store it on disk or send it over the network
#the bytes can then be translated back into an object such as JSON,XML

from .models import Post

from django import forms

#this format is the same as serializer
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = {
#             'title',
#             'description'
#         }

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','description']