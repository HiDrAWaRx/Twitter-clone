# Generated by Django 3.0.6 on 2020-06-01 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar_url',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
