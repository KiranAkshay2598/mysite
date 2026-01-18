from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    context = {
        'name' : 'kiran'
    }
    return render(request,'home.html', context=context)

def add(request):
    if request.method == 'POST':
        val1=int(request.POST['num1'])
        val2=int(request.POST['num2'])
        result=val1+val2
        return render(request,'result.html',{'total':result})
    else:
        return redirect('home_url')