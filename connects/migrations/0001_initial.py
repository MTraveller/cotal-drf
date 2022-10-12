# Generated by Django 4.1.2 on 2022-10-11 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connected',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connecter_choice', models.CharField(choices=[('0', '0'), ('1', '1')], default='0', max_length=1)),
                ('connecting_choice', models.CharField(choices=[('0', '0'), ('1', '1')], default='0', max_length=1)),
                ('connecter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connecter', to='profiles.profile')),
                ('connecting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connecting', to='profiles.profile')),
            ],
        ),
    ]
