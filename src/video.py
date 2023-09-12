from googleapiclient.discovery import build
import json
import os


class Video:
    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется id видео.
        Дальше все данные будут подтягиваться по API."""

        api_key: str = os.getenv('API_KEY')
        # создан специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.__video_id = video_id
        # получаем данные о канале
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()

        try:
            # название видео
            self.video_title = video_response['items'][0]['snippet']['title']
            # количество просмотров
            self.view_count = int(video_response['items'][0]['statistics']['viewCount'])
            # количество лайков
            self.like_count = int(video_response['items'][0]['statistics']['likeCount'])
        except IndexError:
            self.video_title = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        """
        Выводит название видео
        """
        return self.video_title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        """
        Экземпляр инициализируется id видео и id плейлиста
        """
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        """
        Выводит название видео
        """
        return self.video_title

