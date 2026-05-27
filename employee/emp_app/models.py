from django.db import models

class EmployeeModel(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField()
    emp_salary = models.IntegerField()
    emp_phone = models.CharField(max_length=15)
    emp_address = models.TextField()
    emp_join_date = models.DateField()
    emp_gender = models.CharField(max_length=10)
    emp_age = models.IntegerField()
    emp_leave = models.IntegerField()

    def __str__(self):
        return self.emp_name