# Generated by Django 4.1.2 on 2022-11-26 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linktree',
            name='username',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='social',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
