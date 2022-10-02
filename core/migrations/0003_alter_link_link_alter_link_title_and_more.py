# Generated by Django 4.1.1 on 2022-10-02 14:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_social_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link',
            field=models.CharField(max_length=255, validators=[django.core.validators.URLValidator]),
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('Employee', 'Employee'), ('Job Seeker', 'Job Seeker'), ('Open To Collaborate', 'Open To Collaborate'), ('Owner', 'Owner')], default='Not Specified', max_length=19, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='name',
            field=models.CharField(choices=[('Instagram', 'Instagram'), ('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('Snapchat', 'Snapchat'), ('TikTok', 'TikTok'), ('Telegram', 'Telegram'), ('Dribble', 'Dribble'), ('Pinterest', 'Pinterest'), ('Reddit', 'Reddit'), ('SoundCloud', 'SoundCloud'), ('DeviantArt', 'DeviantArt')], max_length=10),
        ),
        migrations.AlterField(
            model_name='social',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
