# Generated by Django 3.2.8 on 2021-11-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_education_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='startdate',
            field=models.DateField(),
        ),
    ]
