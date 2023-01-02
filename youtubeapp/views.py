from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Channel, Video, Log

class Ranking(View):
    def get(self, request):
        data = {
            'channel': Channel.objects.all().order_by('subscriber_count').reverse()
            }
        return render(request, 'index.html', data)

    def post(self, request):
        pass

class DetailProfile(View):
    def get(self, request, pk):
        channel = Channel.objects.get(pk=pk)
        video = channel.video

        data = {
            'channel': channel,
            'video': video
            }
        return render(request, 'detail.html', data)

    def post(self, request):
        pass