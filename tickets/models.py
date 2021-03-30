from django.db import models
from employee.models import Employee
from clients.models import Clients
# Create your models here.

PRIORITY_CHOICES = (
    (1, 'High'),
    (2, 'Medium'),
    (3, 'Low'),
)

STATUS_CHOICES = (
    (1, 'Open'),
    (2, 'Reopened'),
    (3, 'On Hold'),
    (4, 'Pending'),
    (5, 'InProgress'),
    (6, 'Canceled'),
    (7, 'Solved'),
    (8, 'New'),
)
# class Status(models.TextChoices):
#     Open = "1"
#     Reopened = "2"
#     OnHold = "3"
#     Pending = "4"
#     InProgress = '5'
#     Cancelled = "6"
#     Solved = "7"
#     New = "8"


class Tickets(models.Model):
    ticket_subjects = models.CharField(max_length=200)
    assign_staff = models.CharField(max_length=200, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, null=True, default=2)
    status = models.IntegerField(choices=STATUS_CHOICES, default=8)
    clients = models.ForeignKey(Clients, on_delete=models.DO_NOTHING)
    description = models.TextField()
    file_upload = models.FileField(null=True, blank=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.ticket_subjects

