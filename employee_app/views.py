
from ast import Return
from datetime import datetime
from multiprocessing import context
from ssl import DefaultVerifyPaths
from unicodedata import name
from django import http
from django.shortcuts import redirect, render,HttpResponse
from.models import Employee,Department,Role
from datetime import datetime
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect, render,HttpResponse

def login1(request):
    return render(request,'login.html')


def home1(request):
    return render(request,'home.html')


def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("/index")
            else:
                return HttpResponse("<h1>You are not an admin.</h1>")
        else:
            alert = True
            return render(request, "login.html", {'alert':alert})
    return render(request, "login.html")
# Create your views here.
def index(request):
    return render(request,'index.html')


def all_emp(request):
    emps=Employee.objects.all()
    context= {
        'emps': emps
    }
    print(context)
    return render(request,'view_all_emp.html',context)


def add_emp(request):
    if request.method == "POST":
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        salary= int(request.POST['salary'])
        Bonus= int(request.POST['Bonus'])
        dept= int(request.POST['dept'])
        Role= int(request.POST['Role'])
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,Bonus=Bonus,dept_id=dept,Role_id=Role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('employee added sucessfully')
    elif request.method=='GET':
        
        return render(request,'add_emp.html')
    else:
        return HttpResponse('An exception occure Employee has not been added')



def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
          emp_to_be_removed = Employee.objects.get(id=emp_id)
          emp_to_be_removed.delete()
          return HttpResponse('Employee removed sucessfully')
        except:
          return HttpResponse("Please enter a valid ID")

    emps = Employee.objects.all()
    context= {
        'emps': emps
    }
    print(context)
    return render(request,'remove_emp.html',context)



def filter_emp(request):

    if request.method == 'POST':
        name=request.POST['name']
        dept=request.POST['dept']
        Role=request.POST['Role']
        emps=Employee.objects.all()
        if name:
            emps =emps.filter(Q(first_name__icontains =name) |  Q(last_name__icontains =name))
        if dept:
            emps=emps.filter(dept__name=dept)

        if Role:
            emps=emps.filter(dept__name=Role)


        context = {
            'emps': emps
        }
        

        return render(request,'view_all_emp.html',context)


    elif request.method =='GET':
        return render(request,'filter_emp.html')

    else:
        return HttpResponse('An Exception Occured')
    

def user_logout(request):
    logout(request)
    return redirect('login1')