from django.urls import path
from .views import RegisterView, UserDetailView,CustomAuthToken, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
