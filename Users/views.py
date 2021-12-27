from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUp, UpdateUser, profileUdateForm
from .models import Profile



# Create your views here.
def profile(request):
    return render(request, 'Users/profile.html')

def loginPage(request):
    form = AuthenticationForm()
    context = {'form': form, 'Heading':'Lets Login'}

    next = ''
    if request.GET:
        next = request.GET['next']
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request,user)
                if next == "":
                    return redirect('profile')

                else:
                    return redirect(next)
            else:
                messages.warning(request, "username & password didn't matched")

    return render(request, 'Users/login.html', context)


def register(request):
    form = SignUp()
    context = {'form' : form, 'Heading':'Register Yourself'}

    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created")
            user1 = form.cleaned_data.get('username')
            user_obj = User.objects.filter(username = user1)[0]
            Profile.objects.create(user = user_obj)
            return redirect('login')

    return render(request, 'Users/login.html',context)

def updateProfile(request):
    try:
        if request.method == 'POST':
            user_form =  UpdateUser(request.POST, instance=request.user)
            profile_form = profileUdateForm(request.POST, request.FILES, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Profile Updates')
                return redirect('profile')
        else:
            user_form =  UpdateUser(instance=request.user)
            profile_form = profileUdateForm(instance=request.user.profile)
            context = {'user_form': user_form, 'profile_form': profile_form}
            return render(request, 'Users/updateUser.html',context)
    except User.profile.RelatedObjectDoesNotExist:
        messages.info(request, 'Profile created refresh again')
        Profile.objects.create(user = request.user)
    except Exception as e:
        print(e, type(e))


def user_pass_change_form(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user, data= request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,'Password Changed')
                return redirect('profile')
    
    form = PasswordChangeForm(user = request.user)
    context={'form':form, 'Heading':'Update your password'}
    return render(request, 'Users/login.html',context)
