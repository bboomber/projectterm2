# Generated by Django 2.1.5 on 2019-05-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0003_tranfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='insure',
            name='confirm',
            field=models.IntegerField(default=1),
        ),
    ]
