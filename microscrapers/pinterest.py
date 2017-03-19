import time
from collections import OrderedDict

from Scraper import MicroScraper


class PinterestLogin(MicroScraper):
    def __init__(self, credentials):
        print "Logging in"
        self.credentials = credentials

        #self.login_button_xpath = '//button[@class="//headerLoginButton active"]'
        expectedText = "Log"
        self.login_button_xpath = "//button[contains(text(),'"+expectedText+"')]"
        self.email_xpath = '//input[@type="email"]'
        self.password_xpath = '//input[@type="password"]'
        self.submit_xpath = "//button[@type='submit']"

    def login(self, driver):

        print "Loging in"
        elem = driver.find_element_by_xpath(self.login_button_xpath)
        elem.click()

        username_element = driver.find_element_by_xpath(self.email_xpath)
        username_element.send_keys(self.credentials.getUser())

        password = driver.find_element_by_xpath(self.password_xpath)
        password.send_keys(self.credentials.getPassword())

        login_attempt = driver.find_element_by_xpath(self.submit_xpath)
        login_attempt.submit()
        time.sleep(5)


class Links(object):
    def __init__(self):
        self._relatedPins = []
        self._boards = []
        #self._relatedPins.append(self._url)
#todo figure out how to keep order of definitions
class BoardCollector(Links):
    def __init__(self):
        super(BoardCollector, self).__init__()




    def _getBoards(self):
        boards = self._driver.find_elements_by_css_selector('div.AggregatedCloseupCard.Module.inDidIt')
        for board in boards:
            board_link = board.find_element_by_css_selector("a[href*='pin']")
            self._boards.append(board_link.get_attribute("href"))

    def _getRelatedPins(self):
        related_pins = self._driver.find_elements_by_class_name("pinHolder")
        for pin in related_pins:
            link = pin.find_element_by_class_name("pinImageWrapper")
            href = link.get_attribute("href")
            return Navigator(href)
            self._driver.get(link.get_attribute("href"))

    def _getBoardSummarys(self):
        board_summarys = self._driver.find_elements_by_css_selector('div.boardSummary')
        for summary in board_summarys:
            link = "www.pinteret.com" + summary.get_attribute("href")
            self._relatedPins.append(link)

    def getBoardPin(self):
        pass

    def printLinks(self):
        for link in self._links:
            print link

#Build data base save ability with mongodb
class saveDataBase(object):
    def getImage(self):
        # todo save image to disk
        elem = self._driver.find_element_by_xpath('//img[@class="pinImage rounded"]')
        if elem:
            print elem.get_attribute('data-src')



        # save db
#Friday test run
class Crawler(object):
    def __init__(self):
        #todo test Crawler
        counter = 0
        while ((self._relatedPins != 0) or counter < 5):
            counter +=1
            url = self._relatedPins.pop()
            #Navigate to what I want
            self._driver.get(url)
            #Get related pins
            self._getRelatedPins()

            #Click Main Pin and then get image
            self._getImage()

            #Get Pin's board
            self._getBoards()

            #Go to boards
            self._getBoardSummarays()

            #Get Related Pins