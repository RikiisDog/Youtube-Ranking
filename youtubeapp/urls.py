from django.urls import path
from .views import Ranking, DetailProfile

app_name = 'youtubeapp'

urlpatterns = [
    path('', Ranking.as_view(), name='index'),
    path('detail/<int:pk>', DetailProfile.as_view(), name='detail')
]
