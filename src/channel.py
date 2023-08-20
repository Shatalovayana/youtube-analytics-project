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
        channel = Channel.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.youtube = build('youtube', 'v3', developerKey=os.environ['API_KEY'])
        # название канала
        self.__name = сhannel.get('items')[0].get('snippet').get('title')
        # описание канала
        self.__description = сhannel.get('items')[0].get('snippet').get('description')
        # custom URL канала
        self.__customURL = сhannel.get('items')[0].get('snippet').get('customUrl')
        # Общее количество просмотров
        self.__viewCount = int(сhannel.get('items')[0].get('statistics').get('viewCount'))
        # Количество подписчиков
        self.__subscriberCount = int(сhannel.get('items')[0].get('statistics').get('subscriberCount'))
        # Количество видео на канале
        self.__videoCount = int(сhannel.get('items')[0].get('statistics').get('videoCount'))

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
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