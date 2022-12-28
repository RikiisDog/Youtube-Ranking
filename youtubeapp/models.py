from django.db import models

# Create your models here.

class Data(models.Model):
    channel_name = models.CharField(max_length=100, null=True, blank=True)
    thumbnail = models.URLField(null=True, blank=True)
    channel_url = models.URLField(null=True, blank=True)
    registrant_num = models.IntegerField(null=True, blank=True)
    good_num = models.IntegerField(null=True, blank=True)
    video_num = models.IntegerField(null=True, blank=True)
    publishedat = models.DateTimeField(null=True, blank=True)
    video_url1 = models.URLField(null=True, blank=True)
    video_url2 = models.URLField(null=True, blank=True)
    video_url3 = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.channel_name

class ChannelID(models.Model):
    channel_id = models.CharField(max_length=24)
    channel_name = models.OneToOneField(
        Data,
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )

    def __str__(self):
        return self.channel_name

class Log(models.Model):
    enter = models.CharField(max_length=200)

    def __str__(self):
        return self.enter