from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = auth.authenticate(username=username,password=password)


        if  user is not None:
            auth.login(request, user)
            return redirect('index')

        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    elif request.method == 'GET':
        return render(request,'login.html')   
def register(request):

    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        
    elif request.method == 'GET':
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('index')