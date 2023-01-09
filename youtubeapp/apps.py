from django.apps import AppConfig


class YoutubeappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'youtubeapp'

    def ready(self):
        from .tasks.task import start
        start()
