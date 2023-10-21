"""
Класс для работы с конфигурационным файлом
"""
import settings


class Configuration:
    """
    Класс для работы с конфигурационным файлом
    """

    def __init__(self):
        """
        Конструктор
        """
        self._config: dict = settings.CONFIGURATIONS

    def get(self, key):
        """
        Получить значение по ключу
        """
        return self._config[key]
