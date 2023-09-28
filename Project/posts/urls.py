from django.urls import path
from .views import PostViewSet

app_name = 'posts'

urlpatterns = [
    path('posts', PostViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('posts/<str:pk>', PostViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),        
]
