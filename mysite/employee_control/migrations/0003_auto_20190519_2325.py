# Generated by Django 2.1.5 on 2019-05-19 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_control', '0002_auto_20190519_2304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'permissions': [('is_admin', 'Role is admin'), ('is_manager', 'Role is manager')]},
        ),
    ]
