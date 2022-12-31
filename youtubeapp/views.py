from django.shortcuts import render
from django.views.generic import View
from .models import ChannelID, Channel, Video, Log

# Create your views here.
class Test(View):
    template_name = 'index.html'
    def post(self, request):
        pass
    def get(self, request):
        testdata = {'youtubedata': Channel.objects.all()}
        return render(request, 'index.html', testdata)