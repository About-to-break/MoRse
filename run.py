from parser import Browser

browser = Browser()
browser.run_browser()
print("Откройте требуемую страницу, по завершении нажмите Enter")

ART = """
M       M   OOO    RRRRR    SSSS   EEEEE
MM     MM  O   O   R    R  S       E    
M M   M M  O   O   RRRRR    SSSS   EEEE 
M  M M  M  O   O   R  R         S  E    
M   M   M   OOO    R   R   SSSSS   EEEEE

                V.0.0.1
"""

MENU = """

Welcome to MoRse. Choose between these options:
st - start/restart varnish Firefox process
of - close program
rf - enable auto page refreshing


"""

class MoRse:

    def __init__(self):
        self.browser = None
        self.page_locked = False
        self.memo = None

    def _open_browser(self):
        self.page_locked = False
        self.browser = Browser()
        self.page_locked = self.browser.run_browser()

    def _refresh_page(self):
        if self.browser is not(None) and self.page_locked:
            self.browser.refresh()




    def run(self):
        do_run = True

        print(ART)
        print(MENU)

        while do_run:
            command = input('->')

            if command == 'st':
                self._open_browser()
                break
            elif command == 'of':
                do_run = False
                break
            else:
                print(f'Unknown command "{command}"')



