from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .forms import SignUp



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
            return redirect('login')

    return render(request, 'Users/login.html',context)
