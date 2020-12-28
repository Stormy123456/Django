"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('employeeAdd/',views.employeeAdd),
    path('employeeAddnewdata/',views.employeeAddnewdata,name='employeeAddnewdata'),
    path('employeeBoard/',views.employeeBoard),
    path('employeeEdit/',views.employeeEdit,name='employeeEdit'),
    path('employeeUpdate/',views.employeeUpdate,name='employeeUpdate'),
    path('employeeDelete/',views.employeeDelete,name='employeeDelete'),
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('registerNewdata/',views.registerNewdata,name='registerNewdata'),
    path('logincheck/',views.logincheck,name='logincheck'),
    path('userindex/',views.userindex),
    path('userconfirm/',views.userconfirm),
    path('userAddconfirm/',views.userAddconfirm,name='userAddconfirm'),
    path('logout/',views.logout,name='logout'),
    path('typeuserBoard/',views.typeuserBoard,name='typeuserBoard'),
    path('typeuserAdd/',views.typeuserAdd,name='typeuserAdd'),
    path('typeuserAddnewdata/',views.typeuserAddnewdata,name='typeuserAddnewdata'),
    path('typeuserEdit/',views.typeuserEdit,name='typeuserEdit'),
    path('typeuserUpdate/',views.typeuserUpdate,name='typeuserUpdate'),
    path('typeuserDelete/',views.typeuserDelete,name='typeuserDelete'),
    path('userBoard/',views.userBoard,name='userBoard'),
    path('userDelete/',views.userDelete,name='userDelete'),
    path('adminconfirm/',views.adminconfirm,name='adminconfirm'),
    path('adminAddconfirm/',views.adminAddconfirm,name='adminAddconfirm'),
    path('facultyBoard/',views.facultyBoard,name='facultyBoard'),
    path('facultyAdd/',views.facultyAdd,name='facultyAdd'),
    path('facultyAddnewdata/',views.facultyAddnewdata,name='facultyAddnewdata'),
    path('facultyEdit/',views.facultyEdit,name='facultyEdit'),
    path('facultyUpdate/',views.facultyUpdate,name='facultyUpdate'),
    path('facultyDelete/',views.facultyDelete,name='facultyDelete'),
    path('majorBoard/',views.majorBoard,name='majorBoard'),
    path('majorAdd/',views.majorAdd,name='majorAdd'),
    path('majorAddnewdata/',views.majorAddnewdata,name='majorAddnewdata'),
    path('majorEdit/',views.majorEdit,name='majorEdit'),
    path('majorUpdate/',views.majorUpdate,name='majorUpdate'),
    path('majorDelete/',views.majorDelete,name='majorDelete'),
    path('userReservation/',views.userReservation,name='userReservation'),
    path('userReservationAdd/',views.userReservationAdd,name='userReservationAdd'),
    # path('userReservationDelete/',views.userReservationDelete,name='userReservationDelete'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# if settings.DEBUG :
#     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#     urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
