from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField(unique=True, max_length=4, null=False, blank=False)
    empname = models.CharField(max_length=30, null=False, blank=False)
    emp_email = models.EmailField(unique=True, null=False, blank=False)
    emp_ph = models.IntegerField(unique=True, max_length=10, null=False, blank=False)
    emp_job = models.CharField(null=False, blank=False)
    emp_sal = models.IntegerField(null=False, blank=False)
    emp_DOJ = models.DateField(null=False, blank=False)
    emp_address = models.TextField()

    def __str__(self):
        return f'{self.empid} - {self.empname}'