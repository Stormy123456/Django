from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import employee,users,typeuser,faculty,major,reservation
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
from django import forms
from django.shortcuts import get_object_or_404
import mysql.connector
import mariadb
import sys
import hashlib
import os

# Create your views here.


def index(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            return render(request,'index.html',{})
        else:
            return redirect("/")


def majorBoard(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            data = major.objects.all()
            return render(request,'majorBoard.html',{'mjrdata':data})
        else:
            return redirect("/")

def majorAdd(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            return render(request,'majorAdd.html')
        else:
            return redirect("/")


def majorAddnewdata(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            mjr_name = request.POST['mjr_name']
            content = major(mjr_name=mjr_name)
            if(major.objects.filter(mjr_name=mjr_name)):
                messages.success(request, 'ชื่อสาขานี้ถูกใช้ไปแล้ว')
                return redirect("/majorAdd")
            else:
                content.save()
                messages.success(request, 'บันทึกข้อมูลสำเร็จ')
                return redirect("/majorBoard")
        else:
            return redirect("/")

def majorEdit(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            result = major.objects.filter(pk=id)
            return render(request,'majorEdit.html',{'result':result})
        else:
            return redirect("/")

def majorUpdate(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            if request.method == 'POST':
                id = request.POST['id']
                olddata = major.objects.get(pk = id)
                oldname = olddata.mjr_name
                mjr_name = request.POST['mjr_name']
                content = major.objects.get(pk = id)
                content.mjr_name = ' '
                content.save()
                content = major.objects.get(pk = id)
                content.mjr_name = mjr_name
                result = major.objects.filter(pk=id)
                if(major.objects.filter(mjr_name=mjr_name)):
                    content = major.objects.get(pk = id)
                    content.mjr_name = oldname
                    content.save()
                    messages.success(request, 'ชื่อสาขานี้ถูกใช้ไปแล้ว')
                    return render(request, 'majorEdit.html',{'result':result})
                else:
                    content.save()
                    messages.success(request, 'แก้ไขข้อมูลสำเร็จ')
                    return redirect("/majorBoard")   
            elif request.method == 'GET':
                pass
        else:
            return redirect("/")

def majorDelete(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            major.objects.filter(id=id).delete()
            return redirect("/majorBoard")
        else:
            return redirect("/")

def facultyBoard(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            data = faculty.objects.all()
            return render(request,'facultyBoard.html',{'facdata':data})
        else:
            return redirect("/")

def facultyAdd(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            return render(request,'facultyAdd.html')
        else:
            return redirect("/")


def facultyAddnewdata(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            fac_name = request.POST['fac_name']
            content = faculty(fac_name=fac_name)
            if(faculty.objects.filter(fac_name=fac_name)):
                messages.success(request, 'ชื่อคณะนี้ถูกใช้ไปแล้ว')
                return redirect("/facultyAdd")
            else:
                content.save()
                messages.success(request, 'บันทึกข้อมูลสำเร็จ')
                return redirect("/facultyBoard")
        else:
            return redirect("/")

def facultyEdit(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            result = faculty.objects.filter(pk=id)
            return render(request,'facultyEdit.html',{'result':result})
        else:
            return redirect("/")

def facultyUpdate(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            if request.method == 'POST':
                id = request.POST['id']
                olddata = faculty.objects.get(pk = id)
                oldname = olddata.fac_name
                fac_name = request.POST['fac_name']
                content = faculty.objects.get(pk = id)
                content.fac_name = ' '
                content.save()
                content = faculty.objects.get(pk = id)
                content.fac_name = fac_name
                result = faculty.objects.filter(pk=id)
                if(faculty.objects.filter(fac_name=fac_name)):
                    content = faculty.objects.get(pk = id)
                    content.fac_name = oldname
                    content.save()
                    messages.success(request, 'ชื่อคณะนี้ถูกใช้ไปแล้ว')
                    return render(request, 'facultyEdit.html',{'result':result})
                else:
                    content.save()
                    messages.success(request, 'แก้ไขข้อมูลสำเร็จ')
                    return redirect("/facultyBoard")   
            elif request.method == 'GET':
                pass
        else:
            return redirect("/")

def facultyDelete(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            faculty.objects.filter(id=id).delete()
            return redirect("/facultyBoard")
        else:
            return redirect("/")

def typeuserBoard(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            data = typeuser.objects.all()
            return render(request,'typeuserBoard.html',{'typdata':data})
        else:
            return redirect("/")

def typeuserAdd(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            return render(request,'typeuserAdd.html')
        else:
            return redirect("/")

def typeuserAddnewdata(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            
            typ_name = request.POST['typ_name']
            content = typeuser(typ_name=typ_name)
            if(typeuser.objects.filter(typ_name=typ_name)):
                messages.success(request, 'ชื่อประเภทนี้ถูกใช้ไปแล้ว')
                return redirect("/typeuserAdd")
            else:
                content.save()
                messages.success(request, 'บันทึกข้อมูลสำเร็จ')
                return redirect("/typeuserBoard")
        else:
            return redirect("/")

def typeuserEdit(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            result = typeuser.objects.filter(pk=id)
            return render(request,'typeuserEdit.html',{'result':result})
        else:
            return redirect("/")

def typeuserUpdate(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            if request.method == 'POST':
                id = request.POST['id']
                olddata = typeuser.objects.get(pk = id)
                oldname = olddata.typ_name
                typ_name = request.POST['typ_name']
                content = typeuser.objects.get(pk = id)
                content.typ_name = ' '
                content.save()
                content = typeuser.objects.get(pk = id)
                content.typ_name = typ_name
                result = typeuser.objects.filter(pk=id)
                if(typeuser.objects.filter(typ_name=typ_name)):
                    content = typeuser.objects.get(pk = id)
                    content.typ_name = oldname
                    content.save()
                    messages.success(request, 'ชื่อนี้ถูกใช้ไปแล้ว')
                    return render(request, 'typeuserEdit.html',{'result':result})
                else:
                    content.save()
                    messages.success(request, 'แก้ไขข้อมูลสำเร็จ')
                    return redirect("/typeuserBoard")   
            elif request.method == 'GET':
                pass
        else:
            return redirect("/")

def typeuserDelete(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            typeuser.objects.filter(id=id).delete()
            return redirect("/typeuserBoard")
        else:
            return redirect("/")

def employeeBoard(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            empdata = employee.objects.all()
            return render(request,'employeeBoard.html',{'empdata':empdata})
        else:
            return redirect("/")


def employeeAdd(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            return render(request,'employeeAdd.html')
        else:
            return redirect("/")

def employeeAddnewdata(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
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
        else:
            return redirect("/")

def employeeEdit(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            result = employee.objects.filter(pk=id)
            return render(request,'employeeEdit.html',{'result':result})
        else:
            return redirect("/")


def employeeUpdate(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
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
        else:
            return redirect("/")

def employeeDelete(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            employee.objects.filter(id=id).delete()
            return redirect("/employeeBoard")
        else:
            return redirect("/")

def login(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return render(request,'login.html')
    else:
        if (x == 2):
            return render(request,'userindex.html',{})
        elif (x == 1):
            return render(request,'index.html',{})
        else:
            return redirect("/")

def register(request):
    types = typeuser.objects.all()
    return render(request,'register.html',{'types':types})

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
    user_type = request.POST['user_type']
    finger1 = None
    finger2 = None
    status = 2
    content = users(user_username=user_username,user_password=user_password,user_prefix=user_prefix,user_fname=user_fname,user_lname=user_lname,user_identification_code=user_identification_code,user_type=user_type,user_bdate=user_bdate,user_image=user_image,status_login=status,user_finger1=finger1,user_finger2=finger2)
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
        res2 = employee.objects.filter(emp_username=username,emp_password=password).count()
        if res > 0 and res2 == 0:
            data = users.objects.filter(user_username=username,user_password=password).get()
            request.session['logged_in']=data.status_login
            request.session['id_user']=data.id
            return redirect("/userindex")
        elif res2 > 0 and res == 0:
            data = employee.objects.filter(emp_username=username,emp_password=password).get()
            request.session['logged_in']=data.status_login
            request.session['id_user']=data.id
            return redirect("/index")
        else:
            messages.error(request,"ไม่พบผู้ใช้นี้")
            return redirect("/")
    return render(request, 'login.html')

def userindex(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            return render(request,'userindex.html',{})
        else:
            return redirect("/")

def userconfirm(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            return render(request,'userconfirm.html')
        else:
            return redirect("/")
    

def userAddconfirm(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            if request.method == 'POST':
                id = request.session.get('id_user')
                finger1 = request.POST['finger1']
                finger2 = request.POST['finger2']
                content = users.objects.get(pk = id)
                content.user_finger1 = finger1
                content.user_finger2 = finger2
                content.user_status_finger = True
                
                if(finger1 == '' or finger1 == None or finger2 == '' or finger2 == None):
                    messages.success(request, 'กรุณายืนยันลายนิ้วมือก่อนบันทึก')
                    return render(request, 'userconfirm.html',{})
                else:
                    messages.success(request, 'คุณได้ยืนยันลายนิ้วมือเรียบร้อยแล้ว')
                    content.save()
                    return redirect("/userindex")   
            elif request.method == 'GET':
                pass
        else:
            return redirect("/")
    
def logout(request):
    del request.session['logged_in']
    del request.session['id_user']
    return redirect("/")

def userBoard(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            userdata = users.objects.all()
            return render(request,'userBoard.html',{'userdata':userdata})
        else:
            return redirect("/")

def adminconfirm(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            result = users.objects.filter(pk=id)
            return render(request,'adminconfirm.html',{'result':result})
        else:
            return redirect("/")

def adminAddconfirm(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            if request.method == 'POST':
                id = request.POST['id_user']
                finger1 = request.POST['finger1']
                finger2 = request.POST['finger2']
                content = users.objects.get(pk = id)
                content.user_finger1 = finger1
                content.user_finger2 = finger2
                content.user_status_finger = True
                
                if(finger1 == '' or finger1 == None or finger2 == '' or finger2 == None):
                    messages.success(request, 'กรุณายืนยันลายนิ้วมือก่อนบันทึก')
                    result = users.objects.filter(pk=id)
                    return render(request,'adminconfirm.html',{'result':result})
                else:
                    messages.success(request, 'ยืนยันลายนิ้วมือเรียบร้อยแล้ว')
                    content.save()
                    return redirect("/userBoard")   
            elif request.method == 'GET':
                pass
        else:
            return redirect("/")

def userDelete(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 1):
            id = request.GET['id']
            users.objects.filter(id=id).delete()
            return redirect("/userBoard")
        else:
            return redirect("/")

def userReservation(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            return render(request,'userReservation.html')
        else:
            return redirect("/")

def userReservationAdd(request):
    x = request.session.get('logged_in')
    if ('logged_in' in request.session)==False:
        return redirect("/")
    else:
        if (x == 2):
            if request.method == 'POST':
                rev_userid = request.session.get('id_user')
                rev_roomid = request.POST['rev_roomid']
                rev_date = request.POST['rev_date']
                rev_timestart = request.POST['rev_timestart']
                rev_timestop = request.POST['rev_timestop']
                data = users.objects.get(pk=rev_userid)
                rev_finger1 = data.user_finger1
                rev_finger2 = data.user_finger1
                content = reservation(rev_userid=rev_userid,rev_roomid=rev_roomid,rev_date=rev_date,rev_timestart=rev_timestart,rev_timestop=rev_timestop,rev_finger1=rev_finger1,rev_finger2=rev_finger2)
                content.save()
                messages.success(request, 'จองห้องเรียบร้อยแล้ว')
                return redirect("/userindex")
            elif request.method == 'GET':
                pass
        else:
            return redirect("/")

# def userReservationDelete(request):
#     x = request.session.get('logged_in')
#     if ('logged_in' in request.session)==False:
#         return redirect("/")
#     else:
#         if (x == 2):
#             id = request.GET['id']
#             users.objects.filter(id=id).delete()
#             return redirect("/userBoard")
#         else:
#             return redirect("/")
    
  
    



 
   
