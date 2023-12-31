# Generated by Django 4.2.6 on 2023-10-29 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_myuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_pic',
            field=models.FileField(blank=True, default='users_pics/default.jpg', null=True, upload_to='users_pics'),
        ),
    ]
