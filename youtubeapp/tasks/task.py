from apscheduler.schedulers.background import BackgroundScheduler
from ..youtube.youtube_data_api import YoutubeApiClient
from ..models import Channel, Video, Log

#定期的にyoutube data apiよりデータを取得し、データベースのレコードを更新する
#期間は12時間に1回とし、遅延許容範囲は60*60msとする
def get_execution():

    #チャンネルIDを取得 -> list
    channel_id_list = Channel.objects.all().values('channel_id')
    channel_id = [l.get('channel_id') for l in channel_id_list]
    #インスタンスオブジェクト格納用リストを定義
    object_list = [''] * len(channel_id)

    for cnt, obj in enumerate(channel_id):
        print(obj)

        object_list[cnt] = YoutubeApiClient(obj)
        channel = object_list[cnt].get_channel()
        video = object_list[cnt].get_video()

        #チャンネル更新
        Channel.objects.update_or_create(
            channel_id = obj,
            defaults = {
                'channel_name': channel['title'],
                'channel_url': channel['channel_url'],
                'thumbnail': channel['thumbnail'],
                'subscriber_count': channel['subscriber_count'],
                'video_count': channel['video_count'],
                'view_count': channel['view_count'],
                'published_at': channel['published_at']
            }
        )

        #pk取得
        pk_obj = Channel.objects.get(channel_id=obj)
        pk = pk_obj.id

        #ビデオ更新
        Video.objects.update_or_create(
            channel_id = pk,
            defaults = {
                'channel_id': pk,
                'video_title1': video[0]['title'],
                'video_url1': video[0]['url'],
                'video_thumbnail1': video[0]['thumbnail'],
                'video_view_count1': video[0]['view_count'],
                'video_published_at1': video[0]['published_at'],
                'video_title2': video[1]['title'],
                'video_url2': video[1]['url'],
                'video_thumbnail2': video[1]['thumbnail'],
                'video_view_count2': video[1]['view_count'],
                'video_published_at2': video[1]['published_at'],
                'video_title3': video[2]['title'],
                'video_url3': video[2]['url'],
                'video_thumbnail3': video[2]['thumbnail'],
                'video_view_count3': video[2]['view_count'],
                'video_published_at3': video[2]['published_at'],
                'video_title4': video[3]['title'],
                'video_url4': video[3]['url'],
                'video_thumbnail4': video[3]['thumbnail'],
                'video_view_count4': video[3]['view_count'],
                'video_published_at4': video[3]['published_at'],
                'video_title5': video[4]['title'],
                'video_url5': video[4]['url'],
                'video_thumbnail5': video[4]['thumbnail'],
                'video_view_count5': video[4]['view_count'],
                'video_published_at5': video[4]['published_at'],
                'video_title6': video[5]['title'],
                'video_url6': video[5]['url'],
                'video_thumbnail6': video[5]['thumbnail'],
                'video_view_count6': video[5]['view_count'],
                'video_published_at6': video[5]['published_at']
            }
        )

def start():
    scheduler = BackgroundScheduler()

    scheduler.add_job(
        get_execution,
        trigger='interval',
        hours=12,
        misfire_grace_time=60*60
        )

    scheduler.start()