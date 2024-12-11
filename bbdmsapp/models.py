from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re

# Custom email validator
email_validator = EmailValidator(message="Please enter a valid email address.")
# Custom username validator for alphanumeric characters and underscores
username_validator = RegexValidator(r'^[a-zA-Z0-9_]+$', message="Username must contain only letters, numbers, and underscores.")

class CustomUser(AbstractUser):
    USER = {
        (1, 'admin'),
        (2, 'donor'),
        (3, 'requester'),
    }
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')

    # Overriding the clean method to add validation logic
    def clean(self):
        # Validate email using Django's built-in validator
        try:
            validate_email(self.email)
        except ValidationError:
            raise ValidationError({'email': 'Please enter a valid email address.'})

        # Validate username using a custom regex (allow only alphanumeric and underscores)
        if not re.match("^[A-Za-z0-9_]*$", self.username):
            raise ValidationError({'username': 'Username must contain only letters, numbers, and underscores.'})

    # Override the save method to ensure clean() is called before saving
    def save(self, *args, **kwargs):
        self.clean()  # Call clean method to validate fields
        super(CustomUser, self).save(*args, **kwargs)


class Bloodgroup(models.Model):
    bloodgroup = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DonorReg(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    age = models.IntegerField(default=0)
    mobilenumber = models.CharField(max_length=11)
    bloodgroup = models.ForeignKey(Bloodgroup, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    status = models.CharField(max_length=50, default=0)
    regdate_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BloodRequest(models.Model):
    donid = models.ForeignKey(DonorReg, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=250)
    mobno = models.CharField(max_length=10)
    email = models.EmailField(max_length=250)
    requirer = models.CharField(max_length=250)
    message = models.TextField(max_length=250)
    regdate_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    fullname = models.CharField(max_length=250)
    mobno = models.CharField(max_length=11)
    email = models.EmailField(max_length=250)
    message = models.TextField(max_length=250)
    status = models.CharField(max_length=50)
    regdate_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
