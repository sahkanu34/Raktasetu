from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import  logout,login,authenticate
from django.contrib.auth.decorators import login_required
from bbdmsapp.models import CustomUser,Bloodgroup,DonorReg,BloodRequest
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
from django.core.mail import get_connection
import os


def is_strong_password(password):
    """Check if the password is strong based on specified criteria."""
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):  # Check for uppercase letters
        return False
    if not re.search(r"[a-z]", password):  # Check for lowercase letters
        return False
    if not re.search(r"[0-9]", password):  # Check for digits
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # Check for special characters
        return False
    return True


def validate_age(age):
    if age < 18:
        raise ValidationError('You must be at least 18 years old to register as a donor.')
    if age > 65:  # Adding upper limit for safety
        raise ValidationError('Maximum age for blood donation is 65 years.')

def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Please use .jpg, .jpeg, or .png files.')

def validate_name(value):
    if not re.match("^[a-zA-Z ]+$", value):
        raise ValidationError('Name can only contain letters and spaces.')

def DONORSIGNUP(request):
    bg = Bloodgroup.objects.all()
    if request.method == "POST":
        try:
            # Get all form fields
            pic = request.FILES.get('pic')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            mobno = request.POST.get('mobno')
            age = request.POST.get('age')
            bg_id = request.POST.get('bg_id')
            gender = request.POST.get('gender')
            address = request.POST.get('address')
            password = request.POST.get('password')

            # Profile picture validation
            if not pic:
                messages.error(request, 'Profile picture is required')
                return redirect('donorsignup')
            
            ext = os.path.splitext(pic.name)[1].lower()
            if ext not in ['.jpg', '.jpeg', '.png']:
                messages.error(request, 'Only .jpg, .jpeg, or .png files are allowed for profile picture')
                return redirect('donorsignup')

            # Name validation
            if not first_name.replace(' ', '').isalpha():
                messages.error(request, 'First name should only contain letters')
                return redirect('donorsignup')

            if not last_name.replace(' ', '').isalpha():
                messages.error(request, 'Last name should only contain letters')
                return redirect('donorsignup')

            # Username validation
            if not re.match("^[a-zA-Z0-9_]{3,20}$", username):
                messages.error(request, 'Username must be 3-20 characters and can only contain letters, numbers, and underscores')
                return redirect('donorsignup')

            # Email validation
            if not re.match(r'^[a-zA-Z0-9._%+-]+@(gmail|yahoo)\.com$', email.lower()):
                messages.error(request, 'Please use a valid Gmail or Yahoo email address')
                return redirect('donorsignup')

            # Mobile number validation
            if not re.match("^[0-9]{10}$", mobno):
                messages.error(request, 'Mobile number must be exactly 10 digits')
                return redirect('donorsignup')

            # Age validation
            try:
                age_num = int(age)
                if age_num < 18 or age_num > 65:
                    messages.error(request, 'Age must be between 18 and 65 years')
                    return redirect('donorsignup')
            except ValueError:
                messages.error(request, 'Please enter a valid age')
                return redirect('donorsignup')

            # Blood group validation
            if not bg_id:
                messages.error(request, 'Please select a blood group')
                return redirect('donorsignup')

            # Gender validation
            if not gender:
                messages.error(request, 'Please select a gender')
                return redirect('donorsignup')

            # Address validation
            if not address.strip():
                messages.error(request, 'Address is required')
                return redirect('donorsignup')

            # Password validation
            if len(password) < 8:
                messages.error(request, 'Password must be at least 8 characters long')
                return redirect('donorsignup')
            if not re.search("[A-Z]", password):
                messages.error(request, 'Password must contain at least one uppercase letter')
                return redirect('donorsignup')
            if not re.search("[a-z]", password):
                messages.error(request, 'Password must contain at least one lowercase letter')
                return redirect('donorsignup')
            if not re.search("[0-9]", password):
                messages.error(request, 'Password must contain at least one number')
                return redirect('donorsignup')
            if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
                messages.error(request, 'Password must contain at least one special character')
                return redirect('donorsignup')

            # Check existing email/username
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'This email is already registered')
                return redirect('donorsignup')
            
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken')
                return redirect('donorsignup')

            # If all validations pass, create the user
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                user_type=2,
                profile_pic=pic,
            )
            user.set_password(password)
            user.save()

            # Create donor profile
            bg_instance = Bloodgroup.objects.get(id=bg_id)
            blooddonor = DonorReg(
                admin=user,
                age=age,
                mobilenumber=mobno,
                bloodgroup=bg_instance,
                gender=gender,
                address=address,
            )
            blooddonor.save()

            messages.success(request, 'Registration successful! You can now login.')
            return redirect('donorsignup')

        except Exception as e:
            messages.error(request, f'An error occurred during registration: {str(e)}')
            return redirect('donorsignup')

    context = {
        'bg': bg
    }
    return render(request, 'donor/donor-signup.html', context)
User = get_user_model()


@login_required(login_url='/')
def BLOODREQUESTDETAILS(request):
    donor_admin = request.user
    donor_id = DonorReg.objects.get(admin=donor_admin)
    bloodreq = BloodRequest.objects.filter(donid=donor_id)
    context = {'bloodreq':bloodreq,

    }
    return render(request,'donor/view-request.html',context)

login_required(login_url='/')
def DONORPROFILE(request):
    bg = Bloodgroup.objects.all()
    donor = DonorReg.objects.get(admin = request.user.id)
    context = {
        "donor":donor,
        "bg":bg,
    }
    return render(request,'donor/donor-profile.html',context)

@login_required(login_url='/')
def DONOR_PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        mobilenumber = request.POST.get('mobilenumber')
        bloodgroup_id = request.POST.get('bloodgroup')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            donor = DonorReg.objects.get(admin=request.user.id)
            bloodgroup = Bloodgroup.objects.get(id=bloodgroup_id)
            
            customuser.first_name = first_name
            customuser.last_name = last_name
            donor.age = age
            donor.mobilenumber = mobilenumber
            donor.bloodgroup = bloodgroup
            donor.gender = gender
            donor.address = address
            
            if profile_pic:
                customuser.profile_pic = profile_pic
                
            customuser.save()
            donor.save()
            
            messages.success(request, "Your profile has been updated successfully")
            return redirect('donor-profile')

        except ObjectDoesNotExist:
            messages.error(request, "Profile update failed: User or Donor not found.")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

    return render(request, 'donor/donor-profile.html')