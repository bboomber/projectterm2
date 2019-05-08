# Generated by Django 2.1.5 on 2019-05-08 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package_control', '__first__'),
        ('customer', '__first__'),
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tranfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('pic_balance', models.CharField(max_length=30)),
                ('Package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package_control.Package')),
                ('cus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
    ]
