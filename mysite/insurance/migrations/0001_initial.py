# Generated by Django 2.1.5 on 2019-05-10 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee_control', '0001_initial'),
        ('customer', '0001_initial'),
        ('package_control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_nbr', models.CharField(max_length=30, null=True)),
                ('car_number', models.CharField(max_length=15, null=True)),
                ('company_order', models.CharField(max_length=30, null=True)),
                ('price', models.FloatField()),
                ('total_price', models.FloatField()),
                ('post_date', models.DateField(null=True)),
                ('agent_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_control.Employee')),
                ('car_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Car')),
                ('cus_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
                ('package_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='package_control.Package')),
            ],
        ),
        migrations.CreateModel(
            name='Tranfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('pic_balance', models.ImageField(upload_to='')),
                ('Package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package_control.Package')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_control.Employee')),
            ],
        ),
    ]
