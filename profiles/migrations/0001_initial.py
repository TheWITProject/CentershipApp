# Generated by Django 3.2.12 on 2022-05-03 21:10

from django.conf import settings
import django.contrib.auth.models
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('professional_interests', models.TextField(null=True)),
                ('personal_interests', models.TextField(null=True)),
                ('username', models.CharField(max_length=80, unique=True)),
                ('email', models.CharField(max_length=80)),
                ('password1', models.CharField(max_length=80)),
                ('password2', models.CharField(max_length=80)),
                ('user_type', models.CharField(choices=[('mentee', 'Mentee'), ('mentor', 'Mentor')], max_length=80, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('education', models.CharField(max_length=80, null=True)),
                ('professional_experience', models.TextField(null=True)),
                ('mentee_limit', models.IntegerField(null=True)),
                ('mentorship_duration', models.DurationField(null=True)),
                ('professional_interests', models.CharField(choices=[('Technical Interviews', 'Technical Interviews'), ('Web Development', 'Wed Development'), ('App Development', 'App Development'), ('Math', 'Math'), ('Computer Science', 'Computer Science'), ('Science', 'Science'), ('Engineering', 'Engineering')], max_length=80, null=True)),
                ('personal_interests', models.CharField(choices=[('Painting', 'Painting'), ('Music', 'Music'), ('Photogrpahy', 'Photography'), ('Reading', 'Reading'), ('Sports', 'Sports'), ('Cooking', 'Cooking')], max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('goals', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None)),
                ('professional_interests', models.CharField(choices=[('Technical Interviews', 'Technical Interviews'), ('Web Development', 'Wed Development'), ('App Development', 'App Development'), ('Math', 'Math'), ('Computer Science', 'Computer Science'), ('Science', 'Science'), ('Engineering', 'Engineering')], max_length=80, null=True)),
                ('personal_interests', models.CharField(choices=[('Painting', 'Painting'), ('Music', 'Music'), ('Photogrpahy', 'Photography'), ('Reading', 'Reading'), ('Sports', 'Sports'), ('Cooking', 'Cooking')], max_length=80, null=True)),
                ('mentor', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.mentor')),
            ],
        ),
    ]
