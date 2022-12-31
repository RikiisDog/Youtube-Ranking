from django.db import models

GAME = (
    ('1', 'APEX LEGENDS'),
    ('2', 'CLASH ROYALE'),
    ('3', 'FORTNITE'),
    ('4', 'VALORANT'),
    ('5', 'SUPER SMASH BROS'),
    ('6', 'STREAMER')
    )

class ChannelID(models.Model):
    channel_name = models.CharField(max_length=255)
    channel_id = models.CharField(max_length=24)
    category = models.CharField(max_length=255, choices=GAME)

    def __str__(self):
        return self.channel_name

    class Meta:
        db_table = 'ChannelID'



class Video(models.Model):
    video_title1 = models.CharField(max_length=255, null=True, blank=True)
    video_url1 = models.URLField(null=True, blank=True)
    video_thumbnail1 = models.URLField(null=True, blank=True)
    video_view_count1 = models.PositiveIntegerField(null=True, blank=True)
    video_published_at1 = models.CharField(max_length=11, null=True, blank=True)

    video_title2 = models.CharField(max_length=255, null=True, blank=True)
    video_url2 = models.URLField(null=True, blank=True)
    video_thumbnail2 = models.URLField(null=True, blank=True)
    video_view_count2 = models.PositiveIntegerField(null=True, blank=True)
    video_published_at2 = models.CharField(max_length=11, null=True, blank=True)

    video_title3 = models.CharField(max_length=255, null=True, blank=True)
    video_url3 = models.URLField(null=True, blank=True)
    video_thumbnail3 = models.URLField(null=True, blank=True)
    video_view_count3 = models.PositiveIntegerField(null=True, blank=True)
    video_published_at3 = models.CharField(max_length=11, null=True, blank=True)

    video_title4 = models.CharField(max_length=255, null=True, blank=True)
    video_url4 = models.URLField(null=True, blank=True)
    video_thumbnail4 = models.URLField(null=True, blank=True)
    video_view_count4 = models.PositiveIntegerField(null=True, blank=True)
    video_published_at4 = models.CharField(max_length=11, null=True, blank=True)

    video_title5 = models.CharField(max_length=255, null=True, blank=True)
    video_url5 = models.URLField(null=True, blank=True)
    video_thumbnail5 = models.URLField(null=True, blank=True)
    video_view_count5 = models.PositiveIntegerField(null=True, blank=True)
    video_published_at5 = models.CharField(max_length=11, null=True, blank=True)

    video_title6 = models.CharField(max_length=255, null=True, blank=True)
    video_url6 = models.URLField(null=True, blank=True)
    video_thumbnail6 = models.URLField(null=True, blank=True)
    video_view_count6 = models.PositiveIntegerField(null=True, blank=True)
    video_published_at6 = models.CharField(max_length=11, null=True, blank=True)


    class Meta:
        db_table = 'Video'



class Channel(models.Model):
    channel_name = models.CharField(max_length=255, null=True)
    channel_url = models.URLField(null=True, blank=True)
    thumbnail = models.URLField(null=True, blank=True)
    subscriber_count = models.PositiveIntegerField(null=True, blank=True)
    video_count = models.PositiveIntegerField(null=True, blank=True)
    view_count = models.PositiveIntegerField(null=True, blank=True)
    published_at = models.CharField(max_length=11, null=True, blank=True)
    video = models.ForeignKey(
                            Video,
                            on_delete=models.CASCADE,
                            related_name='video'
                            )
    channel_id = models.ForeignKey(
                                ChannelID,
                                on_delete=models.CASCADE,
                                related_name='channnel_id'
                                )

    def __str__(self):
        return self.channel_name

    class Meta:
        db_table = 'Channel'
        ordering = ['subscriber_count']



class Log(models.Model):
    enter = models.CharField(max_length=255)

    def __str__(self):
        return self.enter

    class Meta:
        db_table = 'Log'