# Generated by Django 4.1.3 on 2022-11-25 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAS', '0005_remove_userinfo_cpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='cpassword',
            field=models.CharField(default='000', max_length=64, verbose_name='cpassword'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='totalclass',
            field=models.IntegerField(default=10, verbose_name='totalclass'),
        ),
    ]
