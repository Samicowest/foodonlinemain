from django.shortcuts import render, HttpResponse, redirect
from .forms import UserForm
from django.contrib import messages 
from vendor.forms import VendorForm
from . models import User, UserProfile

# Create your views here.
def registeruser(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            # password = form.cleaned_data.get('password')
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = user.CUSTOMER 
            user.save()
            messages.success(request, "Your account has been registered successfully")

            # Create the user using create user method 

            return redirect('registerUser')
    else:
        form = UserForm() 
    context = {
        'form':form,

    }
    return render(request, 'accounts/registeruser.html', context)

def registerVendor(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.VENDOR
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile 
            vendor.save()
            messages.success(request, 'Your account have been regigstered successfully! Please wait for the approval.')
    else:
        form = UserForm()
        v_form = VendorForm()
    
    context = {
        'form':form,
        'v_form':v_form,
    }
    return render(request, 'accounts/registerVendor.html', context)
