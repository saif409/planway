from django.db import models
from django.contrib.auth.models import User
from clients.models import ClientsProject

# Create your models here.
ROLE_CHOICES = (
    (1, 'Managing Director'),
    (2, 'CEO'),
    (3, 'HR'),
    (4, 'CTO'),
    (5, 'Project Manager'),
    (6, 'Team Leader'),
    (7, 'Employee'),
)

STATUS_CHOICES = (
    (1, 'Active'),
    (2, 'InActive'),
    (3, 'Rejected'),
)

GENDER_CHOICES = (
    (1, 'Male'),
    (2, 'Female'),
    (3, 'Others'),
)


class Team(models.Model):
    team_name = models.CharField(max_length=200)

    def __str__(self):
        return self.team_name


class EmergencyContact(models.Model):
    name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    phone_another = models.CharField(max_length=20,null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class FamilyInformation(models.Model):
    name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=200)
    nid = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    position = models.CharField(max_length=200)
    organization_name = models.CharField(max_length=200)
    from_date = models.DateField()
    date_to = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.organization_name


class Department(models.Model):
    department_name = models.CharField(max_length=200)
    create_at = models.DateField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.department_name


class Designation(models.Model):
    designation_type = models.CharField(max_length=200)
    department_name = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    created_at = models.DateField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)


    def __str__(self):
        return self.designation_type


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_info')
    profile_picture = models.FileField(null=True,blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee_id = models.IntegerField()
    date_of_join = models.DateField()
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1)
    report_to = models.CharField(max_length=100, null=True)
    passport_no = models.CharField(max_length=100, null=True)
    nationality = models.CharField(max_length=100, null=True)
    religion = models.CharField(max_length=200, null=True)
    martial_status = models.CharField(max_length=100, null=True)
    employment_of_spouse = models.CharField(max_length=200, null=True)
    no_of_chilldren = models.CharField(max_length=200, default=None, null=True,blank=True)
    university_name = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    university_date_form = models.DateField(null=True, blank=True)
    university_date_to = models.DateField(null=True, blank=True)
    bank_name = models.CharField(max_length=200, null=True,blank=True)
    bank_account_no = models.CharField(max_length=200, null=True, blank=True)
    ifsc_code = models.CharField(max_length=200, null=True, blank=True)
    pan_no = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    emergency_contact = models.ManyToManyField(EmergencyContact, blank=True)
    family_information = models.ManyToManyField(FamilyInformation, blank=True)
    experience = models.ManyToManyField(Experience, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def contact_information(self):
        return self.emergency_contact.all()

    @property
    def family_info(self):
        return self.family_information.all()

    @property
    def experience_info(self):
        return self.experience.all()

    @property
    def picture_url(self):
        url = ""
        try:
            url = self.profile_picture.url
        except:
            url=""
        return url

    @property
    def leave_enjoyed(self):
        total_leave = 0
        for days in self.leave_set.all():
            total_leave +=days
        return total_leave


class Leader(models.Model):
    leader_name = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leader')
    assign_staff = models.ManyToManyField(Employee, related_name='assign_staff')
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.leader_name.user.username


class Timesheet(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    project_name = models.ForeignKey(ClientsProject, on_delete=models.DO_NOTHING)
    team_leader = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    project_progress = models.IntegerField()
    working_feature = models.CharField(max_length=200)
    working_feature_progress = models.IntegerField()

    def __str__(self):
        return self.employee.user.username





