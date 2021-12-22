# Generated by Django 4.0 on 2021-12-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('genre', models.CharField(choices=[('horror', 'horror'), ('ficsion', 'ficsion'), ('milodram', 'milodram')], max_length=15)),
                ('date', models.DateField()),
                ('actors', models.ManyToManyField(to='movie.Actor')),
            ],
        ),
    ]
