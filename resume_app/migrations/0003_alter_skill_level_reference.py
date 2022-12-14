# Generated by Django 4.0.6 on 2022-09-06 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0002_master_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Link', models.URLField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_app.user')),
            ],
            options={
                'db_table': 'reference',
            },
        ),
    ]
