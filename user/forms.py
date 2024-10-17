from django_registration.forms import RegistrationForm
from .models import CustomUser

class UserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']  # List the fields you want in the form
