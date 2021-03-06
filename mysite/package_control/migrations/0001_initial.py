# Generated by Django 2.1.5 on 2019-05-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_id', models.CharField(max_length=30, null=True)),
                ('package_name', models.CharField(max_length=30, null=True)),
                ('company_name', models.CharField(max_length=30, null=True)),
                ('package_cc', models.IntegerField()),
                ('package_type', models.CharField(max_length=30, null=True)),
                ('price', models.FloatField()),
                ('detail', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion_name', models.CharField(max_length=30)),
                ('promotion_detail', models.CharField(max_length=200)),
                ('end_date', models.DateField(null=True)),
            ],
        ),
    ]
