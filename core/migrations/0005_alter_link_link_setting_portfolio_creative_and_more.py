# Generated by Django 4.1.2 on 2022-10-06 06:30

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_profile_location_alter_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link',
            field=models.URLField(max_length=255),
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='core.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('link', models.URLField(blank=True, max_length=255, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolios', to='core.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Creative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('link', models.URLField(blank=True, max_length=255, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creatives', to='core.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('link', models.URLField(blank=True, max_length=255, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='core.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.models.user_directory_path)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('link', models.URLField(blank=True, max_length=255, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='awards', to='core.profile')),
            ],
        ),
    ]