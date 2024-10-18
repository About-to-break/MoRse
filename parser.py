import time
import random
from selenium import webdriver  # Используем selenium
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import configparser


class Browser:
    def __init__(self):
        # Чтение конфигурации из файла paths.ini
        self.config = configparser.ConfigParser()
        self.config.read('paths.ini')

        # Путь к Firefox и geckodriver
        self.firefox_path = self.config['Paths']['firefox_path']
        self.geckodriver_path = self.config['Paths']['geckodriver_path']

        # Настройки для запуска Firefox
        self.options = Options()
        self.options.binary_location = self.firefox_path

        # Сервис для geckodriver
        self.service = Service(self.geckodriver_path)

        # Переменная для хранения драйвера
        self.driver = None
        # Storage of last html page
        self.memo = None

    def run_browser(self):
        # Запускаем браузер Firefox с geckodriver
        print(f"Запуск браузера Firefox с geckodriver")
        self.driver = webdriver.Firefox(service=self.service, options=self.options)
        print("Браузер запущен. Пожалуйста, зайдите на нужный сайт вручную.")
        input("После того, как вы загрузили страницу, нажмите Enter для продолжения...")
        return True

    def refresh(self):
        try:
            while True:
                # Генерируем случайное время ожидания от 3 до 15 минут
                wait_time = random.uniform(3, 15) * 60  # Переводим минуты в секунды
                print(f">>> Waiting for {wait_time / 60:.2f} minutes to update the page...")

                # Засыпаем на случайное время
                time.sleep(wait_time)

                # Обновляем страницу
                print(">>> Updating the page...")
                self.driver.refresh()
                self._get_page_source()
        except KeyboardInterrupt:
            print('>>> Updating routine cancelled')
        finally:
            if self.driver:
                self.driver.quit()

    def _get_page_source(self):
        """Метод для получения HTML текущей страницы."""
        if self.driver:
            self.memo= self.driver.page_source
            print(">>> HTML has been snatched")
        else:
            print(">>> Couldn't get HTML due to existing drive issue")

    #must be async
    def _check_memo(self):
        if self.memo is not(None):
            pass

