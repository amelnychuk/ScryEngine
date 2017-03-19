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

class Processor(object):

    def __init__(self):
        self._processes = []

    def add(self, microProcess):
        assert isinstance(microProcess, MicroProcess), "{0} is not a MicroProcess".format(microProcess)
        self._process.append(microProcess)

    def run(self, *args, **kwargs):
        for process in self._processes:
            result = process(*args, **kwargs)
            assert isinstance(result, MicroProcess), "{0} is not a MicroProcess".format(result)
            self._process.append(result)


class Scraper(Processor):

    scrape = Processor.run


class MetaProcess(type):

    @classmethod
    def __prepare__(metacls, name, bases):
        return OrderedDict()

    def __new__(metacls, name, bases, namespace, **kwds):
        newclass = type.__new__(metacls, name, bases, dict(namespace))

        newclass._processes = []
        for value in namespace.values():
            if hasattr(value, '_filter'):
                newclass._processes.append(value)
        return newclass


class MicroProcess(metaclass=MetaProcess):
    """
    The base class for scraping objects.
    """

    def __call__(self, *args, **kwargs):

        processes = []
        for _process in self._processes:
            processes.append(_process(self, *args, **kwargs))

        return processes

    def process(func):
        func._filter = True
        return func


class MicroScraper(MicroProcess):

    scraper = MicroProcess.process

class subMicroScraper(MicroScraper):

    @MicroScraper.scraper
    def printSubProcess(self, driver):
        print ("subprocess: ", driver)

class newMicroScraper(MicroScraper):

    @MicroScraper.scraper
    def printpoop(self, driver):
        print ("poop", driver)

    @MicroScraper.scraper
    def dowhatever(self,driver):
        print("Bah", driver)
        return


    def dowhatevertest(self,driver):
        print("No Filter Attribute")





m = newMicroScraper()
m("driver")


