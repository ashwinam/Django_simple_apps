from django.urls import path
from . import views as blogViews

urlpatterns = [
    path('post',blogViews.createPost, name = 'post'),
    path('allpost',blogViews.allpost, name = 'allpost'),
    
]