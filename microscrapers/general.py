import time

from ProcessFactory import MicroProcess, MacroProcess


class Navigator(MicroProcess):
    def __init__(self, url=""):
        self.seturl(url)

    def seturl(self, url):
        self._url = url

    @MicroProcess.process
    def get(self, driver):
        print("Navigating")
        driver.get(self._url)
        time.sleep(2)



class Scrollers(MacroProcess):
    def vertScroll(self, driver):
        prev_scrollHeight = 99999
        while prev_scrollHeight != driver.execute_script("return window.pageYOffset;"):
            prev_scrollHeight = driver.execute_script("return window.pageYOffset;")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)