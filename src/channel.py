from pprint import pprint
from googleapiclient.discovery import build
import os
import json


class Channel:
    """Класс для ютуб-канала"""
    __youtube_object = None

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        Channel.__youtube_object = build('youtube', 'v3', developerKey=os.environ['API_KEY'])
        channel = Channel.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        # название канала
        self.__name = channel.get('items')[0].get('snippet').get('title')
        # описание канала
        self.__description = channel.get('items')[0].get('snippet').get('description')
        # custom URL канала
        self.__customURL = channel.get('items')[0].get('snippet').get('customUrl')
        # Общее количество просмотров
        self.__viewCount = int(channel.get('items')[0].get('statistics').get('viewCount'))
        # Количество подписчиков
        self.__subscriberCount = int(channel.get('items')[0].get('statistics').get('subscriberCount'))
        # Количество видео на канале
        self.__videoCount = int(channel.get('items')[0].get('statistics').get('videoCount'))

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        pprint(channel)

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return Channel.__youtube_object

    def to_json(self):
        """Сохраняет в файл значения атрибутов экземпляра Channel.
        Название файла соответствует названию канала YouTube.
        """
        # Создаем словарь
        channel_dict = {'channel name': self.__name,
                        'channel_id': self.__channel_id,
                        'description': self.__description,
                        'channel URL': self.url,
                        'channel custom URL': self.__customURL,
                        'subscriber count': self.__subscriberCount,
                        'view count': self.__viewCount,
                        'video count': self.__videoCount
                        }
        file_name_list = [self.title, 'json']
        with open('.'.join(file_name_list), 'w', encoding='utf-8') as file:
            json.dump(channel_dict, file, indent=4)

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def title(self):
        return self.__name

    @property
    def video_count(self):
        return self.__videoCount

    @property
    def view_count(self):
        return self.__viewCount

    @property
    def subscriber_count(self):
        return self.__subscriberCount

    @property
    def url(self):
        return 'https://www.youtube.com/channel/' + self.__channel_id

    @property
    def custom_url(self):
        return 'https://www.youtube.com/' + self.__customURL

    @property
    def description(self):
        return self.__description
