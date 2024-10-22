import asyncio
from browser import Browser
from analyzer import Analyzer


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


ART = """
M       M   OOO    RRRRR    SSSS   EEEEE
MM     MM  O   O   R    R  S       E    
M M   M M  O   O   RRRRR    SSSS   EEEE 
M  M M  M  O   O   R  R         S  E    
M   M   M   OOO    R   R   SSSSS   EEEEE

                V.0.0.2
"""

MENU = """

Welcome to MoRse. Choose between these options:
st - start/restart varnish Firefox process
of - close program
rf - enable auto page refreshing


"""


@singleton
class MoRse:

    def __init__(self):
        self.browser = None
        self.page_locked = False
        self.analyzer = Analyzer()

    def _open_browser(self):
        self.page_locked = False
        self.browser = Browser(self.analyzer)
        self.page_locked = self.browser.run_browser()

    async def _refresh_page(self):
        if self.browser is not None and self.page_locked:
            await self.browser.refresh()

    async def run(self):
        do_run = True

        print(ART)
        print(MENU)

        while do_run:
            command = asyncio.get_event_loop().run_in_executor(None, input, '->')

            if command == 'st':
                self._open_browser()
            elif command == 'of':
                do_run = False
            elif command == 'rf':
                await self._refresh_page()
            else:
                print(f'Unknown command "{command}"')


if __name__ == "__main__":
    m = MoRse()
    asyncio.run(m.run())
