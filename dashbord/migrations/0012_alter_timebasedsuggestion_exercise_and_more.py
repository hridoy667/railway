# Generated by Django 5.1.2 on 2024-11-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0011_rename_water_intake_timebasedsuggestion_exercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timebasedsuggestion',
            name='Exercise',
            field=models.CharField(blank=True, help_text='Water intake suggestion', max_length=150),
        ),
        migrations.AlterField(
            model_name='timebasedsuggestion',
            name='diet_suggestion',
            field=models.TextField(blank=True, help_text='Diet suggestions'),
        ),
    ]
