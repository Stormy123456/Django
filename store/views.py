from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import employee,users
from django.db import connection
from django.db import connections
from django.contrib import messages
from django.http import HttpResponseRedirect
import os

# Create your views here.
def index(request):
    return render(request,'index.html')

def employeeBoard(request):
    empdata = employee.objects.all()
    return render(request,'employeeBoard.html',{'empdata':empdata})

def employeeAdd(request):
    return render(request,'employeeAdd.html')

def employeeAddnewdata(request):
    emp_username = request.POST['emp_username']
    emp_password = request.POST['emp_password']
    emp_prefix = request.POST['emp_prefix']
    emp_fname = request.POST['emp_fname']
    emp_lname = request.POST['emp_lname']
    emp_identification_code = request.POST['emp_identification_code']
    emp_bdate = request.POST['emp_bdate']
    emp_image = request.FILES['emp_image']
    content = employee(emp_username=emp_username,emp_password=emp_password,emp_prefix=emp_prefix,emp_fname=emp_fname,emp_lname=emp_lname,emp_identification_code=emp_identification_code,emp_bdate=emp_bdate,emp_image=emp_image)
    
    if(employee.objects.filter(emp_username=emp_username)):
        messages.success(request, 'Username นี้ถูกใช้ไปแล้ว')
        return redirect("/employeeAdd")
    elif(employee.objects.filter(emp_identification_code=emp_identification_code)):
        messages.success(request, 'รหัสประจำตัวประชาชนถูกใช้ไปแล้ว')
        return redirect("/employeeAdd")
    else:
        content.save()
        messages.success(request, 'บันทึกข้อมูลสำเร็จ')
        return redirect("/employeeBoard")

def employeeEdit(request):
    id = request.GET['id']
    result = employee.objects.filter(pk=id)
    return render(request,'employeeEdit.html',{'result':result})


def employeeUpdate(request):
    id = request.POST['id']
    emp_username = request.POST['emp_username']
    emp_password = request.POST['emp_password']
    emp_prefix = request.POST['emp_prefix']
    emp_fname = request.POST['emp_fname']
    emp_lname = request.POST['emp_lname']
    emp_identification_code = request.POST['emp_identification_code']
    emp_bdate = request.POST['emp_bdate']
    try:
        emp_image = request.FILES['emp_image']
    except KeyError:
        emp_image = None
    content = employee.objects.get(pk = id)
    content.emp_username = emp_username
    content.emp_password = emp_password
    content.emp_prefix =  emp_prefix
    content.emp_fname = emp_fname
    content.emp_lname = emp_lname
    content.emp_identification_code = emp_identification_code
    content.emp_bdate = emp_bdate
    if emp_image is not None:
        employee.objects.get(id=id).emp_image.delete(save=True)
        content.emp_image = emp_image
    # if(employee.objects.filter(emp_username=emp_username)):
    #     messages.success(request, 'Username นี้ถูกใช้ไปแล้ว')
    #     return redirect("/employeeUpdate")
    # elif(employee.objects.filter(emp_identification_code=emp_identification_code)):
    #     messages.success(request, 'รหัสประจำตัวประชาชนถูกใช้ไปแล้ว')
    #     return redirect("/employeeUpdate")
    # else:
    #     content.save()
    #     messages.success(request, 'แก้ไขข้อมูลสำเร็จ')
    #     return redirect("/employeeBoard")
    content.save()
    messages.success(request, 'แก้ไขข้อมูลสำเร็จ')
    return redirect("/employeeBoard")



def employeeDelete(request):
    id = request.GET['id']
    employee.objects.filter(id=id).delete()
    return redirect("/employeeBoard")

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def registerNewdata(request):
    user_username = request.POST['user_username']
    user_password = request.POST['user_password']
    user_prefix = request.POST['user_prefix']
    user_fname = request.POST['user_fname']
    user_lname = request.POST['user_lname']
    user_identification_code = request.POST['user_identification_code']
    user_bdate = request.POST['user_bdate']
    user_image = request.FILES['user_image']
    content = users(user_username=user_username,user_password=user_password,user_prefix=user_prefix,user_fname=user_fname,user_lname=user_lname,user_identification_code=user_identification_code,user_bdate=user_bdate,user_image=user_image)
    content.save()
    return redirect("/login")
 
   
