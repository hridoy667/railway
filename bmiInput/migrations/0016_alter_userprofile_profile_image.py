# Generated by Django 5.1.2 on 2024-11-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmiInput', '0015_userprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='profile_pictures/default-profile.jpg', upload_to='profile_pictures/'),
        ),
    ]
