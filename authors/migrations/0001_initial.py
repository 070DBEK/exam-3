# Generated by Django 5.1.5 on 2025-01-26 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Biography')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='URL Slug')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='authors/', verbose_name='Profile Picture')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'unique_together': {('first_name', 'last_name')},
            },
        ),
    ]
