# Generated by Django 3.0.11 on 2020-12-03 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0010_auto_20201203_0045'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
    ]