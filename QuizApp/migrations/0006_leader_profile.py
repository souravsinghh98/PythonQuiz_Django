# Generated by Django 3.0.1 on 2020-04-08 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0005_auto_20200407_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
