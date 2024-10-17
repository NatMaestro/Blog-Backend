"""
URL configuration for BlogApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
# from users.forms import UserForm
from user.forms import UserForm
from django_registration.backends.one_step.views import RegistrationView
# from main.views import Index
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/', RegistrationView.as_view(
                 form_class = UserForm, 
         success_url = "/", 
    ), 
    name=  'register'),

    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('accounts/', include("django.contrib.auth.urls")),# Include the blog app's URL configuration
    path('api/', include('user.urls')),  # Include the blog app's URL configuration
    path('api/', include('articles.urls')),  # Include the blog app's URL configuration
    # path('api/token-auth/', obtain_auth_token, name='api_token_auth'),
    # path('api-auth/', include('rest_framework.urls')), 
]
