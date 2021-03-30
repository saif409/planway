from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Clients(models.Model):
    company_name = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    profile_picture = models.FileField()
    designation = models.CharField(max_length=200)
    clients_id = models.IntegerField()
    phone = models.IntegerField()
    email = models.CharField(max_length=200)
    nid = models.IntegerField()
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name


class ClientsProject(models.Model):
    company_name = models.ForeignKey(Clients, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=200)
    project_deadline = models.DateField()
    project_leader = models.ForeignKey('employee.Leader', on_delete=models.CASCADE, null=True, blank=True)
    project_employee = models.ManyToManyField('employee.Employee')
    progress = models.IntegerField(default=0, null=True,blank=True)
    project_description = models.TextField()
    project_files = models.FileField()
    priority = models.CharField(max_length=200)
    start_date = models.DateField()
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.project_title