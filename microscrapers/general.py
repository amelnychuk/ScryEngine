import time

from Scraper import MicroScraper


class Navigator(MicroScraper):
    def __init__(self, url=""):
        self.seturl(url)

    def seturl(self, url):
        self._url = url

    def get(self,driver):
        print "Navigating"
        driver.get(self._url)
        time.sleep(2)


class Scrollers(MicroScraper):
    def vertScroll(self, driver):
        prev_scrollHeight = 99999
        while prev_scrollHeight != driver.execute_script("return window.pageYOffset;"):
            prev_scrollHeight = driver.execute_script("return window.pageYOffset;")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)