"""firstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Attendence import views as attView
from django.contrib.auth import views as auth_views
from Users import views as userView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', attView.home, name='attHome'),
    path('atten/', include('Attendence.urls')),
    # path('Login/',auth_views.LoginView.as_view(template_name = 'Users/login.html'),name='login'),
    path('Login',userView.loginPage, name='login'),
    path('profile/',userView.profile, name='profile'),
    path('Logout/',auth_views.LogoutView.as_view(template_name = 'Users/logout.html'),name='logout'),
    path('user/',include('Users.urls'))

]
urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)