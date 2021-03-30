# Generated by Django 3.0.5 on 2021-03-23 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsproject',
            name='project_employee',
            field=models.ManyToManyField(to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='clientsproject',
            name='project_leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Leader'),
        ),
    ]