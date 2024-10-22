import random
import asyncio
from analyzer import Analyzer
from selenium import webdriver  # Используем selenium
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import configparser


class Browser:
    def __init__(self, analyzer: Analyzer):
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

        # Переменная для хранения объекта анализатора
        self.analyzer = analyzer

    def run_browser(self):
        # Запускаем браузер Firefox с geckodriver
        print(f"Running Firefox with geckodriver")
        self.driver = webdriver.Firefox(service=self.service, options=self.options)
        print("Please open required URL")
        input("Press Enter after done...")
        return True

    async def refresh(self):
        try:
            while True:
                # Генерируем случайное время ожидания от 3 до 15 минут
                wait_time = random.uniform(3, 15) * 60  # Переводим минуты в секунды
                print(f">>> Waiting for {wait_time / 60:.2f} minutes to update the page...")

                # Засыпаем на случайное время
                await asyncio.sleep(wait_time)
                # Обновляем страницу
                print(">>> Updating the page...")
                self.driver.refresh()
                web_page = self._get_page_source()
                await self.analyzer.check(web_page)

        except KeyboardInterrupt:
            print('>>> Updating routine cancelled')
        finally:
            if self.driver:
                self.driver.quit()

    def _get_page_source(self):
        """Метод для получения HTML текущей страницы."""
        if self.driver:
            web_page = self.driver.page_source
            print(">>> HTML has been snatched")

            return web_page
        else:
            print(">>> Couldn't get HTML due to existing driver issue")

            raise RuntimeError("Check geckodriver and retry")
