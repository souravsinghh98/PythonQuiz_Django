# Generated by Django 3.0.1 on 2020-04-07 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QuizApp', '0002_leader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leader',
            name='username',
        ),
        migrations.AddField(
            model_name='leader',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='leader',
            name='score',
            field=models.IntegerField(),
        ),
    ]
