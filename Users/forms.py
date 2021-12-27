from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from . models import Profile




class SignUp(UserCreationForm):
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UpdateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class profileUdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'image']
        
