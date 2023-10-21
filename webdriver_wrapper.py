import time
from typing import List, Dict, Any, Optional

from selenium.webdriver import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.remote.webelement import WebElement

# Импортирую селениум
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from configuration import Configuration


class WebDriverWrapper:
    """
    Универсальный класс для работы с вебдрайвером
    """

    def __init__(self, configurations: Configuration):
        """
        Конструктор
        """
        self.config_obj: Configuration = configurations
        self.is_proxy: bool = self.config_obj.get_config('is_proxy')
        self.proxy: str = self.config_obj.get_config('proxy')
        self.options: list[str] = self.config_obj.get_config('driver_options')
        self.driver: Optional[webdriver.Chrome] = None
        self.services: Optional[ChromeService] = None
        self.chrome_option_object: Optional[webdriver.ChromeOptions] = None

    def __get_chrome_services(self):
        """
        Функция, которая возвращает сервис для хрома
        """
        self.services = ChromeService(ChromeDriverManager().install())

    def __get_chrome_option_object(self):
        """
        Функция, которая возвращает объект опций для хрома
        """
        self.chrome_option_object = webdriver.ChromeOptions()

    def __add_options_to_chrome(self):
        """
        Функция, которая добавляет опции в хром
        """
        for option in self.options:
            self.chrome_option_object.add_argument(option)

    def __add_proxy(self):
        """
        Функция, которая добавляет прокси в хром
        """

        proxy = Proxy()
        proxy.proxy_type = ProxyType.MANUAL
        proxy.http_proxy = self.proxy
        proxy.ssl_proxy = self.proxy
        self.chrome_option_object.add_argument(f"--proxy-server={self.proxy}")

    def get_chrome_webdriver(self):
        """
        Функция, которая возвращает вебдрайвер хрома
        """
        self.__get_chrome_services()
        self.__get_chrome_option_object()
        self.__add_options_to_chrome()
        if self.is_proxy:
            self.__add_proxy()
        self.driver = webdriver.Chrome(service=self.services, options=self.chrome_option_object)
        return self.driver

    def get_url(self, url: str):
        """
        Функция, которая переходит по ссылке
        """
        self.driver.get(url)
        time.sleep(60)


# Тестируем
if __name__ == '__main__':
    config_obj = Configuration()
    web_driver_wrapper = WebDriverWrapper(config_obj)
    web_driver_wrapper.get_chrome_webdriver()
    web_driver_wrapper.get_url('https://www.sulpak.kz/g/holodilnik_haier_cef535awd/ust_kamenogorsk/')
    web_driver_wrapper.driver.quit()
