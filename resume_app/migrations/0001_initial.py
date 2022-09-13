# Generated by Django 4.0.6 on 2022-08-22 05:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board_University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Location', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Board Or Universities',
                'db_table': 'BoardOrUniversity',
            },
        ),
        migrations.CreateModel(
            name='Course_Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Type', models.CharField(max_length=10)),
                ('Duration', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
            ],
            options={
                'db_table': 'Course Or Stream',
            },
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'master',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.FileField(default='avatar.png', upload_to='users/profile/')),
                ('About', models.TextField(default='', max_length=255)),
                ('FullName', models.CharField(default='', max_length=30)),
                ('Mobile', models.CharField(default='', max_length=10)),
                ('BirthDate', models.DateField(auto_now=True)),
                ('Country', models.CharField(default='', max_length=20)),
                ('State', models.CharField(default='', max_length=20)),
                ('City', models.CharField(default='', max_length=20)),
                ('Address', models.TextField(default='', max_length=255)),
                ('Master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_app.master')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
                ('level', models.IntegerField()),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_app.user')),
            ],
            options={
                'db_table': 'skill',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Category', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=100)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_app.user')),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobTitle', models.CharField(max_length=100)),
                ('Company', models.CharField(max_length=100)),
                ('StartDate', models.DateField(auto_now=True)),
                ('EndDate', models.DateField(auto_now=True)),
                ('Description', models.CharField(max_length=100)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_app.user')),
            ],
            options={
                'db_table': 'experience',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDate', models.DateField(auto_now=True)),
                ('EndDate', models.DateField(auto_now=True)),
                ('Score', models.DecimalField(decimal_places=2, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('IsPercent', models.BooleanField(default=True)),
                ('Description', models.CharField(max_length=100)),
                ('IsCompleted', models.BooleanField(default=False)),
                ('BoardUniversity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_app.board_university')),
                ('CourseStream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_app.course_stream')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_app.user')),
            ],
            options={
                'db_table': 'education',
            },
        ),
    ]
