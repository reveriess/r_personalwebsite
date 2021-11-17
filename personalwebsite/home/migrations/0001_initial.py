# Generated by Django 3.2.8 on 2021-11-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentInterests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_name', models.CharField(max_length=40)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['interest_name'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=40)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['startdate'],
            },
        ),
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_name', models.CharField(max_length=40)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['startdate'],
            },
        ),
        migrations.CreateModel(
            name='StoryPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=40)),
                ('summary', models.TextField()),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]