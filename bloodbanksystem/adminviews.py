from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import  logout,login,authenticate
from django.contrib.auth.decorators import login_required
from bbdmsapp.models import CustomUser,Bloodgroup,DonorReg,Contact,BloodRequest
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .import views
User = get_user_model()



def ADD_BLOODGROUP(request):
    if request.method == "POST":
        bloodgroup = request.POST.get('bloodgroup')
        bloodgroup =Bloodgroup(
            bloodgroup=bloodgroup,
        )
        bloodgroup.save()
        messages.success(request,'Blood Group  Added Succeesfully!!!')
        return redirect("add_bloodgroup")
    return render(request,'admin/add-bloodgroup.html')


@login_required(login_url='/')
def MANAGEBLOODGROUP(request):
    bgrp = Bloodgroup.objects.all()
    context = {'bgrp':bgrp,

    }
    return render(request,'admin/manage-bloodgroup.html',context)

@login_required(login_url='/')
def DELETE_BLOODGROUP(request,id):
    bloodgrp = Bloodgroup.objects.get(id=id)
    bloodgrp.delete()
    messages.success(request,'Record Delete Succeesfully!!!')
    
    return redirect('manage_bloodgroup')

login_required(login_url='/')
def UPDATE_BLOODGROUP(request,id):
    bloodgrp = Bloodgroup.objects.get(id=id)
    
    context = {
         'bloodgrp':bloodgrp,
    }

    return render(request,'admin/edit-bloodgroup.html',context)


login_required(login_url='/')

def UPDATE_BLOODGROUP_DETAILS(request):
        if request.method == 'POST':
          blgrp_id = request.POST.get('bg_id')
          bloodgroup = request.POST.get('bloodgroup')
          bldgrp= Bloodgroup.objects.get(id=blgrp_id) 
          bldgrp.bloodgroup = bloodgroup
          bldgrp.save()   
          messages.success(request,"Your blood group detail has been updated successfully")
          return redirect('manage_bloodgroup')
        return render(request, 'admin/edit-bloodgroup.html')


login_required(login_url='/')

def VIEWDONORLIST(request):
    donor_lists = DonorReg.objects.all()
    context = {'dl':donor_lists,

    }
    return render(request,'admin/donor-list.html',context)

@login_required(login_url='/')
def DELETE_DONOR(request, id):
    try:
        donreg = get_object_or_404(DonorReg, id=id)
        custom_user = donreg.admin  # Access the related CustomUser
        donreg.delete()  # This will also delete the associated CustomUser because of the on_delete=models.CASCADE
        custom_user.delete()
        messages.success(request, 'Record deleted successfully!')
    except Exception as e:
        messages.error(request, f'Error deleting record: {e}')
    return redirect('view_donor_list')

@login_required(login_url='/')
def hide_donor_details(request, id):
    donor = get_object_or_404(DonorReg, id=id)
    donor.status = 'Hide'
    donor.save()
    messages.success(request, 'Detail of Donor is hidden!')
    return redirect('view_donor_list')

@login_required(login_url='/')
def unhide_donor_details(request, id):
    donor = get_object_or_404(DonorReg, id=id)
    donor.status = '0'
    donor.save()
    messages.success(request, 'Detail of Donor is unhidden!')
    return redirect('view_donor_list')

def VIEWCONTACTUSQUERY(request):
    query_lists = Contact.objects.all()
    context = {'ql':query_lists,

    }
    return render(request,'admin/manage-contactusquery.html',context)

@login_required(login_url='/')
def DELETE_CONTACTUSQUERY(request,id):
    query = Contact.objects.get(id=id)
    query.delete()
    messages.success(request,'Record Delete Succeesfully!!!')
    
    return redirect('view_contactus_query')


@login_required(login_url='/')
def PENDINGCONTACTUSQUERY(request,id):
    query = Contact.objects.get(id=id)
    query.status = 'Read'
    query.save()
    messages.success(request,'Read!!!')
    
    return redirect('view_contactus_query')


@login_required(login_url='/')
def BLOODREQUEST(request):
    bloodreq = BloodRequest.objects.all()
    context = {'bloodreq':bloodreq,

    }
    return render(request,'admin/blood-request.html',context)

@login_required(login_url='/')
def DASHBOARD(request):
    bg_count = Bloodgroup.objects.all().count()
    donor_count = DonorReg.objects.all().count()
    br_count = BloodRequest.objects.all().count()
    contact_count = Contact.objects.all().count()
    context = {
        "bg_count": bg_count,
        "donor_count": donor_count,
        "br_count": br_count,
        "contact_count": contact_count,
    }
    return render(request, 'dashboard.html', context)



def Blood_Request_Between_Date_Report(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    bloodreq = []

    if start_date and end_date:
        # Validate the date inputs
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'admin/br-between-date.html', {'bloodreq': bloodreq, 'error_message': 'Invalid date format'})

        # Filter visitors between the given date range
        bloodreq = BloodRequest.objects.filter(regdate_at__range=(start_date, end_date))

    return render(request, 'admin/br-between-date.html', {'bloodreq': bloodreq,'start_date':start_date,'end_date':end_date})