from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import  logout,login,authenticate
from django.contrib.auth.decorators import login_required
from bbdmsapp.models import CustomUser,Bloodgroup,DonorReg,Contact,BloodRequest
from django.contrib.auth import get_user_model

User = get_user_model()

def BASE(request):    
       return render(request,'base.html')


def LOGIN(request):
    return render(request,'login.html')

def doLogout(request):
    logout(request)
    return redirect('login')

def doLogin(request):
    if request.method == 'POST':
        user = authenticate(request,
                                         username=request.POST.get('username'),
                                         password=request.POST.get('password')
                                         )
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                 return redirect('dashboard')
            elif user_type == '2':
                 return redirect('dashboard')
            elif user_type == '3':
                return redirect('dashboard')
            
            
        else:
                messages.error(request,'Username or Password is not valid')
                return redirect('login')
    else:
            messages.error(request,'Username or Password is not valid')
            return redirect('login')

login_required(login_url='/')
def DASHBOARD(request):
    bg_count = Bloodgroup.objects.all().count
    donor_count = DonorReg.objects.all().count
    br_count = BloodRequest.objects.all().count
    contact_count = Contact.objects.all().count
    context = {"bg_count":bg_count,
    "donor_count":donor_count,
    "br_count":br_count,
    "contact_count":contact_count,
        
    }
    return render(request,'dashboard.html',context)


login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {
        "user":user,
    }
    return render(request,'profile.html',context)

@login_required(login_url = '/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        print(profile_pic)
        

        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            

            
            if profile_pic !=None and profile_pic != "":
               customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request,"Your profile has been updated successfully")
            return redirect('profile')

        except:
            messages.error(request,"Your profile updation has been failed")
    return render(request, 'profile.html')




@login_required(login_url = '/')
def CHANGE_PASSWORD(request):
     context ={}
     ch = User.objects.filter(id = request.user.id)
     
     if len(ch)>0:
        data = User.objects.get(id = request.user.id)
        context["data"]:data
     if request.method == "POST":        
        current = request.POST["cpwd"]
        new_pas = request.POST['npwd']
        user = User.objects.get(id = request.user.id)
        un = user.username
        check = user.check_password(current)
        if check == True:
          user.set_password(new_pas)
          user.save()
          messages.success(request,'Password Change  Succeesfully!!!')
          user = User.objects.get(username=un)
          login(request,user)
        else:
          messages.success(request,'Current Password wrong!!!')
          return redirect("change_password")
     return render(request,'change-password.html')
