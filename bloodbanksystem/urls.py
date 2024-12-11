"""
URL configuration for bloodbanksystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views, adminviews, donorviews, userviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('Dashboard', views.DASHBOARD, name='dashboard'),
    path('login', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),
    path('Profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),
    path('Password', views.CHANGE_PASSWORD, name='change_password'),
    

    # Admin Panel
    path('Admin/AddBloodGroup', adminviews.ADD_BLOODGROUP, name='add_bloodgroup'),
    path('Admin/ManageBloodGroup', adminviews.MANAGEBLOODGROUP, name='manage_bloodgroup'),
    path('Admin/DeleteBloodGroup/<str:id>', adminviews.DELETE_BLOODGROUP, name='delete_bloodgroup'),
    path('Admin/UpdateBloodGroup/<str:id>', adminviews.UPDATE_BLOODGROUP, name='update_bloodgroup'),
    path('Admin/UPDATE_BloodGroup_DETAILS', adminviews.UPDATE_BLOODGROUP_DETAILS, name='update_bloodgroup_details'),
    path('Admin/DonorList', adminviews.VIEWDONORLIST, name='view_donor_list'),
    path('Admin/HideDonorlist/<str:id>', adminviews.hide_donor_details, name='hide_donorlist'),
    path('Admin/UnhideDonorlist/<str:id>', adminviews.unhide_donor_details, name='unhide_donorlist'),
    path('Admin/DeleteDonor/<str:id>', adminviews.DELETE_DONOR, name='delete_donor'),
    
    path('Admin/ContactusQuery', adminviews.VIEWCONTACTUSQUERY, name='view_contactus_query'),
    path('Admin/DeleteContactusQuery/<str:id>', adminviews.DELETE_CONTACTUSQUERY, name='delete_contactus_query'),
    path('Admin/PendingContactusQuery/<str:id>', adminviews.PENDINGCONTACTUSQUERY, name='pending_contactus_query'),
    path('Admin/BloodRequest', adminviews.BLOODREQUEST, name='blood-request'),
    path('Admin/BloodRequestBetweenDateReport', adminviews.Blood_Request_Between_Date_Report, name='br_between_date_report'),

    # Donor Panel
    path('donorsignup/', donorviews.DONORSIGNUP, name='donorsignup'),
    path('BloodRequest/', donorviews.BLOODREQUESTDETAILS, name='blood_request'),
    path('DonorProfile', donorviews.DONORPROFILE, name='donor-profile'),
    path('DonorProfile/update', donorviews.DONOR_PROFILE_UPDATE, name='donor-profile_update'),

    # User Panel
    path('userbase/', userviews.USERBASE, name='userbase'),
    path('', userviews.Index, name='index'),
    path('user/bloodrequest/<str:id>', userviews.BLOODREQUEST, name='blood-request'),
    path('user/bloodrequest_Details', userviews.BLOODREQUESTDETAILS, name='blood-request-details'),
    path('user/donorlist', userviews.DONORLIST, name='donor-list'),
    path('user/Aboutus', userviews.ABOUTUS, name="aboutus"),
    path('user/Contactus', userviews.CONTACTUS, name="contactus"),
    path('user/SearchDonor', userviews.SEARCHDONOR, name="search-donor"),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
