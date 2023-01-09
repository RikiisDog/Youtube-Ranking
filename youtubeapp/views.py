from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Channel, Comment
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Ranking(View):
    def get(self, request):
        data = {
            'channel': Channel.objects.all().order_by('subscriber_count').reverse()
            }
        return render(request, 'index.html', data)

    def post(self, request):
        pass


class DetailProfile(View):
    def __paging(self, request, queryset):
        count = 10
        paginator = Paginator(queryset, count)
        page_now = request.GET.get('page')

        try:
            page = paginator.page(page_now)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        return page


    def get(self, request, pk):
        channel = Channel.objects.get(pk=pk)
        video = channel.video
        comment = channel.comment.all().order_by('duedate').reverse()
        form = CommentForm
        page = self.__paging(request,comment)

        data = {
            'channel': channel,
            'video': video,
            'page':page,
            'form':form
            }

        return render(request, 'detail.html', data)


    def post(self, request, pk):
        channel = Comment(channel=Channel.objects.get(pk=pk))
        form = CommentForm(request.POST, instance=channel)

        if form.is_valid():
            form.name = form.cleaned_data['name']
            form.message = form.cleaned_data['message']
            form.channel = pk
            print(form.channel)
            form.save()
            return redirect('youtubeapp:detail', pk=pk)

        return render(request,'detail.html',{'form':form})