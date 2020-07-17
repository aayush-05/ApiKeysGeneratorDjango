from django.urls import path
from .views import generate_key, serve_key, unblock_key, delete_key

urlpatterns = [
    path('generate', generate_key),
    path('serve', serve_key),
    path('unblock', unblock_key),
    path('delete', delete_key),
]
