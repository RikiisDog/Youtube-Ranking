# Generated by Django 4.1.4 on 2023-01-08 03:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeapp', '0003_alter_channel_published_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='名無しさん', max_length=20)),
                ('duedate', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', models.TextField(max_length=50)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='youtubeapp.channel')),
            ],
            options={
                'verbose_name_plural': 'コメント',
                'db_table': 'comment',
            },
        ),
    ]