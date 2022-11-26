# Generated by Django 4.1.2 on 2022-11-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_award_options_alter_certificate_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='slug',
            field=models.SlugField(max_length=80),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='slug',
            field=models.SlugField(max_length=80),
        ),
        migrations.AlterField(
            model_name='creative',
            name='slug',
            field=models.SlugField(max_length=80),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(max_length=80),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(max_length=80),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('Owner', 'Owner'), ('Employee', 'Employee'), ('Job Seeker', 'Job Seeker'), ('Open To Collaborate', 'Open To Collaborate'), ('Hands Full', 'Hands Full'), ('Traveling', 'Traveling'), ('Not Specified', 'Not Specified')], default='Not Specified', max_length=19, null=True),
        ),
    ]
