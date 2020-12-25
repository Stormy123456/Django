from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import employee,users
from django.db import connection
from django.db import connections
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django_file_md5 import calculate_md5
from django.contrib.auth.hashers import make_password
from operator import itemgetter
from django.shortcuts import get_object_or_404
from django.contrib.sessions.models import Session
import mysql.connector
import mariadb
import sys
import hashlib
import os

# Create your views here.
def index(request):
    x = request.session.get('logged_in')
    # return HttpResponse('logged_in' in request.session)
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            # return redirect("/index")
            return render(request,'userindex.html',{})
        elif (x == 1):
            return render(request,'index.html',{})

def employeeBoard(request):
    empdata = employee.objects.all()
    return render(request,'employeeBoard.html',{'empdata':empdata})

def employeeAdd(request):
    return render(request,'employeeAdd.html')

def employeeAddnewdata(request):
    emp_username = request.POST['emp_username']
    emp_password = request.POST['emp_password']
    # emp_password = make_password(password)
    emp_prefix = request.POST['emp_prefix']
    emp_fname = request.POST['emp_fname']
    emp_lname = request.POST['emp_lname']
    emp_identification_code = request.POST['emp_identification_code']
    emp_bdate = request.POST['emp_bdate']
    emp_image = request.FILES['emp_image']
    finger1 = None
    finger2 = None
    status = 1
    content = employee(emp_username=emp_username,emp_password=emp_password,emp_prefix=emp_prefix,emp_fname=emp_fname,emp_lname=emp_lname,emp_identification_code=emp_identification_code,emp_bdate=emp_bdate,emp_image=emp_image,status_login=status,emp_finger1=finger1,emp_finger2=finger2)
    
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
    if request.method == 'POST':
        id = request.POST['id']

        olddata = employee.objects.get(pk = id)
        oldusername = olddata.emp_username
        oldidentification = olddata.emp_identification_code
        oldpassword = olddata.emp_password

        emp_username = request.POST['emp_username']
        emp_password = request.POST['emp_password']
        # if (password != oldpassword):
        #     emp_password = make_password(password)
        # else:
        #     emp_password = oldpassword
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
        content.emp_username = ''
        content.emp_identification_code = ''
        content.save()
        content = employee.objects.get(pk = id)
        content.emp_username = emp_username
        content.emp_password = emp_password
        content.emp_prefix =  emp_prefix
        content.emp_fname = emp_fname
        content.emp_lname = emp_lname
        content.emp_identification_code = emp_identification_code
        content.emp_bdate = emp_bdate
        result = employee.objects.filter(pk=id)
        if emp_image is not None:
            employee.objects.get(id=id).emp_image.delete(save=True)
            content.emp_image = emp_image
        if(employee.objects.filter(emp_username=emp_username)):
            content = employee.objects.get(pk = id)
            content.emp_username = oldusername
            content.emp_identification_code = oldidentification
            content.save()
            messages.success(request, 'Username นี้ถูกใช้ไปแล้ว')
            return render(request, 'employeeEdit.html',{'result':result})
        elif(employee.objects.filter(emp_identification_code=emp_identification_code)):
            content = employee.objects.get(pk = id)
            content.emp_username = oldusername
            content.emp_identification_code = oldidentification
            content.save()
            messages.success(request, 'รหัสประจำตัวประชาชนถูกใช้ไปแล้ว')
            return render(request, 'employeeEdit.html',{'result':result})
        else:
            content.save()
            messages.success(request, 'แก้ไขข้อมูลสำเร็จ')
            return redirect("/employeeBoard")   
    elif request.method == 'GET':
        pass


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
    # user_password = make_password(password)
    user_prefix = request.POST['user_prefix']
    user_fname = request.POST['user_fname']
    user_lname = request.POST['user_lname']
    user_identification_code = request.POST['user_identification_code']
    user_bdate = request.POST['user_bdate']
    user_image = request.FILES['user_image']
    finger1 = None
    finger2 = None
    status = 2
    content = users(user_username=user_username,user_password=user_password,user_prefix=user_prefix,user_fname=user_fname,user_lname=user_lname,user_identification_code=user_identification_code,user_bdate=user_bdate,user_image=user_image,status_login=status,user_finger1=finger1,user_finger2=finger2)
    if(users.objects.filter(user_username=user_username)):
        messages.success(request, 'Username นี้ถูกใช้ไปแล้ว')
        return redirect("/register")
    elif(users.objects.filter(user_identification_code=user_identification_code)):
        messages.success(request, 'รหัสประจำตัวประชาชนถูกใช้ไปแล้ว')
        return redirect("/register")
    else:
        content.save()
        return redirect("/")
    
def logincheck(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        res = users.objects.filter(user_username=username,user_password=password).count()
        if res > 0:  
            data = users.objects.filter(user_username=username,user_password=password).get()
            request.session['logged_in']=data.status_login
            # return HttpResponse(request.session['logged_in'])
            return redirect("/index")
        else:
            messages.error(request,"ไม่พบผู้ใช้นี้")
            return redirect("/")
    return render(request, 'login.html')

def userindex(request):
    return render(request,'userindex.html')

def userconfirm(request):
    return render(request,'userconfirm.html')

def userAddconfirm(request):
    # finger1 = None
    # finger2 = None
    # content = users(finger1= ,finger2 =)
    return redirect("/userindex")   

    # data = request.POST['finger1']
    # content = finger_test3(data_finger1=data)
    # content.save()
    # return HttpResponse("OKKKK")

       
    
  
    



 
   
