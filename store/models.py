from django.db import models
from django.db.models import Model 

# Create your models here.
class employee(models.Model,):

    id = models.CharField(primary_key=True,max_length=20,blank=True, default='')

    def save(self, force_insert=False, force_update=False):
        if self.id == "":
            existing_codes = employee.objects.all().order_by('-id')
            if existing_codes.count() > 0:
                new_code = int(existing_codes[0].id[3:]) + 1
            else:
                new_code = 1
            self.id = 'EMP%03d' % new_code
        super(employee, self).save(force_insert, force_update)
   

    emp_username=models.CharField(max_length=20,unique=True, error_messages={"unique_error_message": u"This username has already been registered."})
    emp_password=models.CharField(max_length=20)
    emp_prefix=models.CharField(max_length=10)
    emp_fname=models.CharField(max_length=20)
    emp_lname=models.CharField(max_length=20)
    emp_identification_code=models.CharField(max_length=13,unique=True)
    emp_bdate=models.DateTimeField()
    emp_image=models.ImageField(upload_to="employee_image",default="")
    

class users(models.Model):

    id = models.CharField(primary_key=True,max_length=20,blank=True, default='')
    def save(self, force_insert=False, force_update=False):
        if self.id == "":
            existing_codes = users.objects.all().order_by('-id')
            if existing_codes.count() > 0:
                new_code = int(existing_codes[0].id[3:]) + 1
            else:
                new_code = 1
            self.id = 'USR%03d' % new_code
        super(users, self).save(force_insert, force_update)
    user_username=models.CharField(max_length=20,unique=True)
    user_password=models.CharField(max_length=20)
    user_prefix=models.CharField(max_length=10)
    user_fname=models.CharField(max_length=20)
    user_lname=models.CharField(max_length=20)
    user_identification_code=models.CharField(max_length=13,unique=True)
    user_bdate=models.DateTimeField()
    user_image=models.ImageField(upload_to="user_image",default="")


