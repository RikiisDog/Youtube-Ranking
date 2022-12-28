from django.contrib import admin
from .models import ChannelID, Data, Log

# Register your models here.
admin.site.register(ChannelID)
admin.site.register(Data)
admin.site.register(Log)