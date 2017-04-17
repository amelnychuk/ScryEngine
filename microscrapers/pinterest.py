import time
import urllib
import os
from collections import OrderedDict

from Executor import Executor
from Museum import Curator
from ScryEngine.microscrapers.general import Navigator, Scrollers

from selenium.webdriver.common.by import By


from pymongo import MongoClient

class PinterestLogin(Executor):
    def __init__(self, credentials):
        print("Logging in")
        self.credentials = credentials

        #self.login_button_xpath = '//button[@class="//headerLoginButton active"]'
        expectedText = "Log"
        self.login_button_xpath = "//button[contains(text(),'"+expectedText+"')]"
        self.email_xpath = '//input[@type="email"]'
        self.password_xpath = '//input[@type="password"]'
        self.submit_xpath = "//button[@type='submit']"

    @Executor.task
    def login(self, driver):

        print("Loging in")
        elem = driver.find_element_by_xpath(self.login_button_xpath)
        elem.click()

        username_element = driver.find_element_by_xpath(self.email_xpath)
        username_element.send_keys(self.credentials.getUser())

        password = driver.find_element_by_xpath(self.password_xpath)
        password.send_keys(self.credentials.getPassword())

        login_attempt = driver.find_element_by_xpath(self.submit_xpath)
        login_attempt.submit()
        time.sleep(2)


class Links(object):
    def __init__(self):
        self._relatedPins = []
        self._boards = []
        #self._relatedPins.append(self._url)

class ImageDataBase(object):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.pinterest
        self.images = self.db.images

    def db_data(self, url, location):

        post = {"url": url,
                "diskPath": location}

        return post




class PinSaver(Executor, Curator):


    #saves data to the images collection

    def __init__(self):
        #super(PinSaver, self).__init__()
        Executor.__init__(self)
        Curator.__init__(self, "pinterest")


    @Executor.task
    def getImage(self, driver):
        elem = driver.find_element_by_xpath('//img[@class="pinImage rounded"]')
        if elem:
            data_src = elem.get_attribute('data-src')

            if not self.exists(data_src):
                print("Saving: ",data_src)

                self.collect(data_src)




class BoardCollector(Executor):
    #body > div.App.AppBase.Module.full > div.appContent > div.mainContainer > div.AggregatedActivityFeed.Module.displayed > div > div > div.feedItems > div.feedContainer.gatorFeed
    @Executor.task
    def _getBoards(self, driver):
        boards = driver.find_elements_by_css_selector('div.AggregatedCloseupCard.Module.inDidIt')
        for board in boards:
            board_link = board.find_element_by_css_selector("a[href*='pin']")
            driver.get(board_link.get_attribute("href"))


            #return Navigator(url= board_link.get_attribute("href"))






            board_container = driver.find_element_by_css_selector("div.feedContainer.gatorFeed")
            board_summarys = board_container.find_elements_by_class_name("boardSummary")
            print(board_summarys)
            #todo test collection with Executors
            Navigators = Executor()
            for summary in board_summarys:
                attr = summary.find_element_by_css_selector('a').get_attribute('href')
                print("myattr: ", attr)
                #link = "www.pinteret.com" + summary.get_attribute("href")
                #print(link)
                Navigators.append(Navigator(url=attr))
                Navigators.append(PinCollector())
            print("REturning", Navigators)
            return Navigators

#todo 3 define Pincollector object

class PinCollector(Executor, Curator):

    def __init__(self):
        Executor.__init__(self)
        Curator.__init__(self, "pinterest")

    counter = 0

    @Executor.task
    def pinHolders(self, driver):
        print("Getting PinHolders")


        Navigators = Executor()
        pinHolders = driver.find_elements_by_css_selector("div.pinHolder")
        print("PinSaver count: ", PinSaver._ids)
        for pinHolder in pinHolders[:10]:
            #refine this to test if the pinboard?
            link = pinHolder.find_element_by_css_selector('a').get_attribute('href')
            #store pinboard in database?
            #todo SUPER IMPORTANT CHECK LINK IN THE DATABASE to avoid infinite loop or have navigator hold urls.
            if not self.exists(link):

                Navigators.append(Navigator(url=link))
                Navigators.append(PinSaver())
                Navigators.append(Scrollers())

                #Navigators.append(BoardCollector())
                #Navigators.append(PinCollector())

            else:
                print("url exists in Curator")
        return Navigators







class relatedPins(Executor):

    def _getRelatedPins(self):
        related_pins = self._driver.find_elements_by_class_name("pinHolder")
        for pin in related_pins:
            link = pin.find_element_by_class_name("pinImageWrapper")
            href = link.get_attribute("href")
            return Navigator(url=href)




        # save db
#Friday test run
class Crawler(object):
    def __init__(self):
        counter = 0
        while ((self._relatedPins != 0) or counter < 5):
            counter +=1

            #Get Pin boards

            #