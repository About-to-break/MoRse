import asyncio


class Analyzer:
    def __init__(self):
        self.memory = None

    async def check(self, web_page):
        if web_page != self.memory:
            await asyncio.sleep(5)
            # Проверить информацию на предмет новой публикации
            return True

        return False

    def make_report(self):
        pass
        # Сформировать отчет
