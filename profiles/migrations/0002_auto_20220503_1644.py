# Generated by Django 3.2.12 on 2022-05-03 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='personal_interests',
        ),
        migrations.RemoveField(
            model_name='user',
            name='professional_interests',
        ),
    ]