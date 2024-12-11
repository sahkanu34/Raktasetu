from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import  logout,login,authenticate
from django.contrib.auth.decorators import login_required
from bbdmsapp.models import CustomUser,DonorReg,BloodRequest,Contact,Bloodgroup
from django.contrib.auth import get_user_model
from django.db.models import Q
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django import forms
import re

def validate_email(value):
    # Adjust the regex according to your requirements
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError(_('Invalid email address: %(value)s'), params={'value': value})

User = get_user_model()

def USERBASE(request):
    
    return render(request, 'userbase.html')

def Index(request):

    donorview = DonorReg.objects.filter(status='0').order_by('-id')[:6]
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        mobno = request.POST.get('mobno')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contactuser =Contact(
            
            fullname=fullname,
            mobno=mobno,
            email=email,
            message=message
            
        )
        contactuser.save()
        messages.success(request,"Thanks for contact with us!!")
        return redirect('index')
    context = {'dv': donorview,
    
    }
    return render(request, 'index.html',context)


def BLOODREQUEST(request,id):
    donorview = DonorReg.objects.get(id=id)
    context = {
         'donview':donorview,
    }
    
    return render(request, 'blood-request.html',context)

def BLOODREQUESTDETAILS(request):
        if request.method == 'POST':
          donor_id = request.POST.get('donor_id')
          fullname = request.POST.get('fullname')
          mobno = request.POST.get('mobno')
          email = request.POST.get('email')
          requirer = request.POST.get('requirer')
          message = request.POST.get('message')
          donorid= DonorReg.objects.get(id=donor_id) 
          requester =BloodRequest(
            donid=donorid,
            fullname=fullname,
            mobno=mobno,
            email=email,
            requirer=requirer,
            message=message
        )
          requester.save()   
          messages.success(request,"Your request blood detail has been sent successfully")
          return redirect('donor-list')
        return render(request, 'blood-request.html')

def DONORLIST(request):
    donorview = DonorReg.objects.filter(status='0')
    context = {'dv': donorview,
    
    }
    return render(request, 'donor-list.html',context)

def ABOUTUS(request):
    return render(request, 'aboutus.html')


def CONTACTUS(request):
    return render(request, 'contactus.html')

def CONTACTUS(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        mobno = request.POST.get('mobno')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contactuser =Contact(
            
            fullname=fullname,
            mobno=mobno,
            email=email,
            message=message
            
        )
        contactuser.save()
        messages.success(request,"Thanks for contact with us!!")
        return redirect('contactus')
    return render(request, 'contactus.html')


def SEARCHDONOR(request):
    bgrp = Bloodgroup.objects.all()
    donorview = DonorReg.objects.all()
    
    if request.method == "GET":
        bloodgrp = request.GET.get('bloodgroup', '')
        location = request.GET.get('location', '')
        
        if bloodgrp or location:
            searchdonor = DonorReg.objects.filter(status='0')
            
            if bloodgrp:
                searchdonor = searchdonor.filter(bloodgroup__bloodgroup__icontains=bloodgrp)
            if location:
                searchdonor = searchdonor.filter(address__icontains=location)
            
            if searchdonor.exists():
                messages.info(request, f"Search results for blood group '{bloodgrp}' and location '{location}'")
            else:
                messages.info(request, "No records found")
                
            return render(request, 'search.html', {'searchdonor': searchdonor, 'bgrp': bgrp, 'dv': donorview, 'bloodgrp': bloodgrp, 'location': location})
    
    context = {'bgrp': bgrp, 'dv': donorview}
    return render(request, 'search.html', context)




   




