# Generated by Django 4.2.6 on 2023-10-18 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profilepics'),
        ),
    ]
