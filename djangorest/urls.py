from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from core.views import PostView, PostListCreateView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('', PostView.as_view(), name='test'),
    path('list-create/', PostListCreateView.as_view(), name='list-create'),
    path('admin/', admin.site.urls),
    path('api/token/', obtain_auth_token, name='obtain-token')
]
