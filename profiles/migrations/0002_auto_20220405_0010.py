# Generated by Django 3.2.12 on 2022-04-05 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('username', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('password1', models.CharField(max_length=80)),
                ('password2', models.CharField(max_length=80)),
            ],
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
    ]
