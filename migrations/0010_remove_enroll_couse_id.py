# Generated by Django 5.0.2 on 2024-02-22 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0009_alter_enroll_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enroll',
            name='couse_id',
        ),
    ]
