# Generated by Django 3.0.5 on 2021-03-23 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=200)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation_type', models.CharField(max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employee.Department')),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('relationship', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('phone_another', models.CharField(max_length=20, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.FileField(blank=True, null=True, upload_to='')),
                ('employee_id', models.IntegerField()),
                ('date_of_join', models.DateField()),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Others')], default=1)),
                ('report_to', models.CharField(max_length=100, null=True)),
                ('passport_no', models.CharField(max_length=100, null=True)),
                ('nationality', models.CharField(max_length=100, null=True)),
                ('religion', models.CharField(max_length=200, null=True)),
                ('martial_status', models.CharField(max_length=100, null=True)),
                ('employment_of_spouse', models.CharField(max_length=200, null=True)),
                ('no_of_chilldren', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('university_name', models.CharField(max_length=200, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('university_date_form', models.DateField(blank=True, null=True)),
                ('university_date_to', models.DateField(blank=True, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=200, null=True)),
                ('bank_account_no', models.CharField(blank=True, max_length=200, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=200, null=True)),
                ('pan_no', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Department')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Designation')),
                ('emergency_contact', models.ManyToManyField(blank=True, null=True, to='employee.EmergencyContact')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200)),
                ('organization_name', models.CharField(max_length=200)),
                ('from_date', models.DateField()),
                ('date_to', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('relationship', models.CharField(max_length=200)),
                ('nid', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Timesheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_leader', models.CharField(max_length=100)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('project_progress', models.IntegerField()),
                ('working_feature', models.CharField(max_length=200)),
                ('working_feature_progress', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employee.Employee')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clients.ClientsProject')),
            ],
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('assign_staff', models.ManyToManyField(related_name='assign_staff', to='employee.Employee')),
                ('leader_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leader', to='employee.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='experience',
            field=models.ManyToManyField(blank=True, null=True, to='employee.Experience'),
        ),
        migrations.AddField(
            model_name='employee',
            name='family_information',
            field=models.ManyToManyField(blank=True, null=True, to='employee.FamilyInformation'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to=settings.AUTH_USER_MODEL),
        ),
    ]
