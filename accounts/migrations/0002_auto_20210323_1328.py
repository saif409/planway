# Generated by Django 3.1.6 on 2021-03-23 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='payment_type',
        ),
        migrations.AddField(
            model_name='payments',
            name='payment_type',
            field=models.IntegerField(choices=[(1, 'Cash'), (2, 'Cheque')], null=True),
        ),
    ]
