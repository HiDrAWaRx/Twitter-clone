# Generated by Django 4.1.10 on 2023-07-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0010_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]