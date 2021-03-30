import datetime
from django.db import models
from django.contrib.auth.models import User
from employee.models import Employee


# Create your models here.

IS_APPROVE = (
    (1, 'New'),
    (2, 'Pending'),
    (3, 'Approve'),
    (4, 'Rejected'),
)


class Leave(models.Model):
    employee_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=500)
    apply_date = models.DateField(auto_now_add=True, )
    leave_from = models.DateField()
    leave_to = models.DateField()
    leave_Reason = models.CharField(max_length=800)
    status = models.IntegerField(choices=IS_APPROVE, null=True, default=2)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.employee_name.user.username

    @property
    def no_of_date(self):
        return (self.leave_to - self.leave_from + datetime.timedelta(1)).days


class TotalLeave(models.Model):
    total = models.IntegerField()
