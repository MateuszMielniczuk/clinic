# Generated by Django 3.0.11 on 2020-12-02 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0007_auto_20201201_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='appointment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='appointment.Appointment'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='appointment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='appointment.Appointment'),
        ),
        migrations.AlterField(
            model_name='visitdescription',
            name='appointment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visit', to='appointment.Appointment'),
        ),
    ]