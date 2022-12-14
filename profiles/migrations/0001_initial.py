# Generated by Django 4.1.2 on 2022-10-07 22:33

import core.upload_to
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=80)),
                ('image', models.ImageField(blank=True, default=None,
                 upload_to=core.upload_to.user_directory_path)),
                ('status', models.CharField(choices=[(None, 'Not Specified'), ('Employee', 'Employee'), ('Job Seeker', 'Job Seeker'), (
                    'Open To Collaborate', 'Open To Collaborate'), ('Owner', 'Owner')], default='Not Specified', max_length=19, null=True)),
                ('location', models.CharField(max_length=50, blank=True)),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('DeviantArt', 'DeviantArt'), ('Dribble', 'Dribble'), (
                    'GitHub', 'GitHub'), ('SoundCloud', 'SoundCloud'), ('Pinterest', 'Pinterest')], max_length=10)),
                ('username', models.CharField(max_length=50, blank=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='socials', to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Profile Activity', max_length=16)),
                ('activity', models.CharField(choices=[
                 ('1', 'Show'), ('0', 'Hide')], default='1', max_length=1)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='settings', to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None,
                 upload_to=core.upload_to.user_directory_path)),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField(max_length=80)),
                ('description', models.CharField(max_length=500)),
                ('link', models.URLField(blank=True, max_length=255)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='portfolios', to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Linktree',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Linktree', max_length=8)),
                ('username', models.CharField(max_length=50, blank=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='linktrees', to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Creative',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField(max_length=80)),
                ('description', models.CharField(max_length=500)),
                ('link', models.URLField(blank=True, max_length=255)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='creatives', to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None,
                 upload_to=core.upload_to.user_directory_path)),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField(max_length=80)),
                ('description', models.CharField(max_length=500)),
                ('link', models.URLField(blank=True, max_length=255)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='certificates', to='profiles.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None,
                 upload_to=core.upload_to.user_directory_path)),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField(max_length=80)),
                ('description', models.CharField(max_length=500)),
                ('link', models.URLField(blank=True, max_length=255)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='awards', to='profiles.profile')),
            ],
        ),
    ]
