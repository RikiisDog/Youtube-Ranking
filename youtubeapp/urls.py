from django.urls import path
from .views import Test

app_name = 'youtubeapp'

urlpatterns = [
    path('index/', Test.as_view(), name='test'),
    path('detail/<int:pk>', Test.as_view(), name='detail')
]
