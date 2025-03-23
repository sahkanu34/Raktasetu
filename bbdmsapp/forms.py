from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import CustomUser
import re

class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password", "password2", "user_type", "profile_pic")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username.isalnum():
            raise ValidationError("Username must contain only letters and numbers.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("Enter a valid email address.")
        
        # Check for common disposable email domains
        disposable_domains = ['example.com', 'test.com', '123.com']  # Add more as needed
        domain = email.split('@')[1]
        if domain in disposable_domains:
            raise ValidationError("Please use a valid email address.")
        
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'\d', password):
            raise ValidationError("Password must contain at least one digit.")
        if not re.search(r'[A-Z]', password):
            raise ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password):
            raise ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError("Password must contain at least one special character.")
        return password