# Generated by Django 4.1.10 on 2023-07-04 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20200602_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='user.png', null=True, upload_to=''),
        ),
    ]