# Generated by Django 4.2.2 on 2023-11-28 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('student_father_name', models.CharField(max_length=30)),
                ('student_mother_name', models.CharField(max_length=30)),
                ('student_dob', models.DateField()),
            ],
        ),
    ]
