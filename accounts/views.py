from django.shortcuts import render, HttpResponse, redirect
from .forms import UserForm
from django.contrib import messages 
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