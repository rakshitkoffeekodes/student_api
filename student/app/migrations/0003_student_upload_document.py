# Generated by Django 4.2.2 on 2023-11-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='upload_document',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]
