from django.urls import path
from . import views as user_views

urlpatterns = [
    path('register',user_views.register, name = 'Register'),
    path('update',user_views.updateProfile, name = 'up_form'),
    path('updatePassword',user_views.user_pass_change_form, name = 'updatepass'),
]