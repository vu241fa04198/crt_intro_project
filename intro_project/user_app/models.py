from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.EmailField(max_length=55)


class  Employeedata(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=255)
    emp_mail = models.EmailField(max_length=55)
    emp_address = models.CharField(max_length=255)
    emp_join_date = models.DateTimeField()
    emp_leave_date = models.DateTimeField()
    emp_gender = models.CharField(max_length=255)
    emp_age = models.EmailField(max_length=55)
