# Generated by Django 4.1.4 on 2023-01-01 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeapp', '0002_remove_channel_video_channel_twitter_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='published_at',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_published_at1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_published_at2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_published_at3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_published_at4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_published_at5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_published_at6',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
