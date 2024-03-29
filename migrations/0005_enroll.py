# Generated by Django 4.2.6 on 2023-10-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0004_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('e_id', models.AutoField(primary_key=True, serialize=False)),
                ('details', models.CharField(max_length=100)),
                ('couse_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.course')),
                ('rollno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.student')),
            ],
        ),
    ]
