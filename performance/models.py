from django.db import models

STATUS_CHOICES = (
    (1, 'Active'),
    (0, 'Inactive'),
)


class GoalType(models.Model):
    goal_type = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.goal_type


class Goal(models.Model):
    goal_type = models.ForeignKey(GoalType, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.CharField(max_length=500, null=True, blank=True)
    target = models.CharField(max_length=500, null=True, blank=True)
    progress = models.FloatField(default=0, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.subject


class TrainingType(models.Model):
    training_type = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.training_type


class Trainer(models.Model):
    first_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    role = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


class Training(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.ForeignKey(TrainingType, on_delete=models.SET_NULL, null=True, blank=True)
    employees = models.ManyToManyField('employee.Employee')
    cost = models.FloatField(default=0)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.trainer


class Promotion(models.Model):
    employee = models.ForeignKey('employee.Employee', on_delete=models.SET_NULL, null=True, blank=True)
    promotion_from = models.ForeignKey('employee.Designation', on_delete=models.SET_NULL, null=True, blank=True)
    promotion_to = models.ForeignKey('employee.Designation', related_name='promotion_to', on_delete=models.SET_NULL, null=True, blank=True)
    promotion_date = models.DateField(null=True, blank=True)

    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.employee


class Resignation(models.Model):
    employee = models.ForeignKey('employee.Employee', on_delete=models.SET_NULL, null=True, blank=True)
    notice_date = models.DateField(null=True, blank=True)
    resignation_date = models.DateField(null=True, blank=True)
    reason = models.TextField(null=True, blank=True)

    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.employee


class TerminationType(models.Model):
    type = models.CharField(max_length=200, null=True, blank=True)

    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.type


class Termination(models.Model):
    employee = models.ForeignKey('employee.Employee', on_delete=models.SET_NULL, null=True, blank=True)
    type = models.ForeignKey(TerminationType, on_delete=models.SET_NULL, null=True, blank=True)
    notice_date = models.DateField(null=True, blank=True)
    termination_date = models.DateField(null=True, blank=True)
    reason = models.TextField(null=True, blank=True)

    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.employee
