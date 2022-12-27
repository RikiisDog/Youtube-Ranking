from django.urls import path
from .views import Test

app_name = 'youtubeapp'

urlpatterns = [
    path('index/', Test.as_view(), name='test'),
]
