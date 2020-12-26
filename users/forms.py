from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
# from .models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    phone_number = forms.CharField(label= "Phone number")
    first_name = forms.CharField(label= "First Name")
    last_name = forms.CharField(label= "Last Name")


    # class Meta:
    #     model = User
    #     fields = ("first_name", "last_name", "email", "phone_number")

# We dont put the login form here because the build-in django login form is enough!