from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    print(request.method)
    print(request.POST)
    name=request.POST.get('name')
    email=request.POST.get('email')
    password=request.POST.get('password')
    contact=request.POST.get('contact')
    # for data create
    Student.objects.create(stu_name=name,stu_email=email,stu_password=password,stu_mobile=contact)
    return HttpResponse("Form Sumbit Successfully..!!")
    # for data read
    data=Student.objects.all()
    print(data)
    return render(request,'home.html',{'key':data})
    
 
