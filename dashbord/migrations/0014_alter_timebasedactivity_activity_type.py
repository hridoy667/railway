# Generated by Django 5.1.2 on 2024-12-01 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0013_alter_timebasedactivity_time_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timebasedactivity',
            name='activity_type',
            field=models.CharField(choices=[('Deep Work', 'Deep Work'), ('Nap', 'Nap'), ('Sleep', 'Sleep')], max_length=20),
        ),
    ]
