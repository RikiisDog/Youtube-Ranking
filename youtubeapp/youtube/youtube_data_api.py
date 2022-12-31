from googleapiclient.discovery import build
from datetime import datetime
import os
import os.path
import dotenv

#環境変数
env = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(env)

#ビルド設定
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
DEVELOPER_KEY = os.environ.get('API_KEY')

class YoutubeApiClient():
    def __init__(self, channel_id):
        self.__client = self.get_youtube_data_api_client()
        self.channel_id = channel_id

    def get_youtube_data_api_client(self):
        return build(
            YOUTUBE_API_SERVICE_NAME,
            YOUTUBE_API_VERSION,
            developerKey=DEVELOPER_KEY
            )

    def get_channel(self) -> dict:
        channel_list = self.__client.channels().list(
            part = 'snippet,statistics',
            id = self.channel_id,
            fields = 'items(id,snippet(title,publishedAt,thumbnails(default(url))),\
            statistics(videoCount,viewCount,subscriberCount))'
            ).execute()

        channel = channel_list['items'][0]
        snippet = channel['snippet']
        statistics = channel['statistics']

        #チャンネル開設日の書式変更
        date_iso = snippet['publishedAt']
        date_conv = datetime.strptime(date_iso, '%Y-%m-%dT%H:%M:%S.%f%z')
        published_at = date_conv.strftime('%Y年%m月%d日')

        #チャンネルURL取得
        channel_url = f"https://www.youtube.com/channel/{channel['id']}"

        return {
            'id': channel['id'],#チャンネルID
            'title': snippet['title'],#チャンネル名
            'channel_url': channel_url,#チャンネルURL
            'thumbnail': snippet['thumbnails']['default']['url'],#チャンネルサムネイル
            'published_at': published_at,#チャンネル開設日
            'subscriber_count': statistics['subscriberCount'],#チャンネル登録者数
            'video_count': statistics['videoCount'],#総動画本数
            'view_count': statistics['viewCount'],#総視聴回数
            }

    def _get_videoid(self) -> list:
        video_list = self.__client.search().list(
            part = 'id',
            channelId = self.channel_id,
            maxResults = 6,
            order = 'viewCount',
            fields = 'items(id(videoId))'
        ).execute()

        video_ids = video_list['items']
        video_id_list = []

        for id in video_ids:
            video_id_list.append(id['id']['videoId'])

        return video_id_list

    def get_video(self) -> dict:

        videos = []
        url = 'https://www.youtube.com/watch?v='
        video_id = self._get_videoid()

        video_list = self.__client.videos().list(
            part = 'snippet, statistics',
            id = ','.join(video_id),
            fields = 'items(snippet(title,thumbnails,publishedAt),statistics(viewCount))'
        ).execute()

        for i, item in enumerate(video_list['items']):
            snippet = item['snippet']
            statistics = item['statistics']

            #チャンネル開設日の書式変更
            date_iso = snippet['publishedAt']
            date_conv = datetime.strptime(date_iso, '%Y-%m-%dT%H:%M:%SZ')
            published_at = date_conv.strftime('%Y年%m月%d日')

            videos.append({
                'title': snippet['title'],
                'url': (url + video_id[i]),
                'thumbnail': snippet['thumbnails']['default']['url'],
                'view_count': statistics['viewCount'],
                'published_at': published_at
            })

        return videos