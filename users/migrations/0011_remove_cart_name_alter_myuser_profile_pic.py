# Generated by Django 4.2.6 on 2023-10-27 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_cart_name_alter_myuser_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profile_pic',
            field=models.ImageField(blank=True, default='users_pics/default.jpg', null=True, upload_to='users_pics'),
        ),
    ]
