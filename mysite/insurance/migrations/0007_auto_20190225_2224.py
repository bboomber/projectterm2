# Generated by Django 2.1.5 on 2019-02-25 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0006_auto_20190225_2117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insure',
            old_name='dec_nbr',
            new_name='doc_nbr',
        ),
    ]