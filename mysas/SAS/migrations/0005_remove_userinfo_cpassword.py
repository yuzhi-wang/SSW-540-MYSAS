# Generated by Django 4.1.3 on 2022-11-25 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SAS', '0004_remove_userinfo_totalclass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='cpassword',
        ),
    ]
