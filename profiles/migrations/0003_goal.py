# Generated by Django 3.2.12 on 2022-05-16 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20220503_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Goal Name')),
                ('achieved', models.BooleanField(default=False, verbose_name='Achieved')),
                ('mentee', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.mentee')),
            ],
        ),
    ]