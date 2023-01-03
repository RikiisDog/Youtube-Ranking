# Generated by Django 4.1.4 on 2023-01-01 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='video',
        ),
        migrations.AddField(
            model_name='channel',
            name='twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='channel',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='youtubeapp.channel'),
        ),
    ]