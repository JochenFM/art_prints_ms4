# Generated by Django 3.2.4 on 2021-09-01 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
