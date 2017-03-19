from selenium import webdriver
from collections import OrderedDict
import functools


class User(object):


    def setUser(self, username):
        self._username = username

    def setPassword(self, password):
        self._password = password

    def getUser(self):
        return self._username

    def getPassword(self):
        return self._password

class RoboBrowser:
    """
    This class does the scraping. It has to be provided Macros



    """

    def __init__(self):


        def chromeDriver():
            chromedriver = "/home/andrew/Projects/03_Pinscraper/webdrivers/chromedriver"
            self._driver = webdriver.Chrome(executable_path=chromedriver)

        chromeDriver()

        self._scrapers = []



    def add(self, scraper):
        """


        :param scaper:
         appends a micro or macroscraper class to this object
        :return:
        """
        assert isinstance(scraper, Scraper), "microscraper is not a Scraper: %r" % scraper
        self._scrapers.append(scraper)

    def scrape(self):
        """

        Loop through all the scrapers and call them. This executes all appended micro and macroscrapers.

        :return:
        """
        #change to a while loop and pop out engines.
        for scraper in self._scrapers:
            engines = scraper(self._driver)
            if engines:
                self._scrapers += engines



