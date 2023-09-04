from django.shortcuts import render , redirect , HttpResponse
from StudentApp.EmailBackend import *
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.


def base(request):
    return render(request , 'base.html' )



def LoginUser(request):
    pass
    return render(request , 'LoginUser.html')

def DoLogin(request):
    if request.user.is_authenticated:
        return redirect('HodHome')
    else: 
        if request.method == "POST":
            username = request.POST.get('email')
            password = request.POST.get('password')
            user = EmailBackend.authenticate(request , username=username , password=password )
            if user!= None:
                if user.is_superuser == True:
                    user_type = "Hod"
                login(request , user)
                user_type = user.user_type
                if user_type == "Hod":
                    return redirect('HodHome')
                elif user_type == "Staff":
                    return redirect('StaffHome')
                elif user_type == "Student":
                    return redirect('StudentHome')
                else:
                    messages.warning(request , 'Invalid Crediential')
                    return redirect('DoLogin')
            else:
                messages.warning(request , 'Invalid Crediential')
                return redirect('DoLogin')
    return render(request , 'LoginUser.html')

def DoLogOut(request):
    logout(request)
    return redirect('DoLogin')

def Profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        'User':user,
    }
    return render(request , 'Profile.html' , context)



def ProfileUpdate(request):
    if request.method == "POST":
        ProfilePic = request.FILES.get('ProfileImage')
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        email = request.POST.get('email')
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            
            customuser.first_name = FirstName
            customuser.last_name = LastName
            
            if ProfilePic != None and ProfilePic != "":
                customuser.profile = ProfilePic
            
            if Password != None and Password != "":
                customuser.set_password(Password)
                
            customuser.save()
            messages.success(request , 'Profile Updated Successfully')
            return redirect('HodHome')   
        
        except:
            messages.error(request , 'Failed to Update Profile')
            return redirect('Profile')
    return render(request , 'Profile.html')