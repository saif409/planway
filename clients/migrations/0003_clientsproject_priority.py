# Generated by Django 3.0.5 on 2021-03-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20210323_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsproject',
            name='priority',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
