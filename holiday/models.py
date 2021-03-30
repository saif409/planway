from django.db import models
from django.utils import timezone
from datetime import date
# Create your models here.


class Holiday(models.Model):
    title = models.CharField(max_length=200)
    holiday_date = models.DateField(auto_now=False)
    day = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    @property
    def in_progress(self):
        return self.holiday_date > date.today()