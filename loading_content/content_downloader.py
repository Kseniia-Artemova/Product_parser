import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from abc import ABC, abstractmethod


class ContentDownloader(ABC):

    def __init__(self):
        self._url = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @url.deleter
    def url(self):
        self._url = None

    @abstractmethod
    def get_content_html(self):
        pass


class ContentDownloaderSamokat(ContentDownloader):

    def __init__(self, header=None):
        super().__init__()
        self._driver = None
        self._header = header
        self._id_for_checking = None

    @property
    def driver(self):
        if self._driver is None:
            self._initialize_driver()
        return self._driver

    @property
    def id_for_checking(self):
        return self._id_for_checking

    @id_for_checking.setter
    def id_for_checking(self, id_for_checking):
        self._id_for_checking = id_for_checking

    @id_for_checking.deleter
    def id_for_checking(self):
        self._id_for_checking = '__NEXT_DATA__'

    def _initialize_driver(self):
        header = self._header if self._header else os.getenv('HEADER')

        chrome_options = Options()
        chrome_options.add_argument(f"user-agent={header}")
        chrome_options.add_argument("--headless")

        if os.getenv('RUNNING_IN_DOCKER'):
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            service = Service(executable_path="/usr/bin/chromedriver")
        else:
            service = Service(ChromeDriverManager().install())

        self._driver = webdriver.Chrome(service=service, options=chrome_options)

    def close_driver(self):
        if self._driver:
            self._driver.quit()
            self._driver = None

    def get_content_html(self):
        try:
            self.driver.get(self._url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self._id_for_checking))
            )
            return self.driver.page_source
        finally:
            self.close_driver()

    def get_content_by_id(self, html_id):
        try:
            self.driver.get(self._url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self._id_for_checking))
            )
            element = self.driver.find_element(By.ID, html_id)
            return element.get_attribute('innerHTML')
        finally:
            self.close_driver()

    def get_product_dict(self, html_id, dict_keys):
        content = self.get_content_by_id(html_id)

        try:
            dict_data = json.loads(content)
        except json.decoder.JSONDecodeError as e:
            print(f'Ошибка декодирования: {e}')
            return
        except TypeError as e:
            print(f'Ошибка декодирования: {e}')
            return

        for dict_key in dict_keys:
            dict_data = dict_data.get(dict_key, False)
            if dict_data is False:
                print('Искомый контент не найден.')
                return
        return dict_data
