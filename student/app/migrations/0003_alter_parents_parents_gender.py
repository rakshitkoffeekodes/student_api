# Generated by Django 4.2.2 on 2023-12-06 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_parentsdata_parents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parents',
            name='parents_gender',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], default=1),
        ),
    ]
