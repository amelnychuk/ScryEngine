from selenium import webdriver

from Executor import Executor, ObjectMaker, Data
from ScryEngine.microscrapers.general import Navigator
from ScryEngine.microscrapers.pinterest import PinterestLogin, BoardCollector, PinSaver, PinCollector
from collections import OrderedDict
import functools

from Museum import Curator

import json
import os


class User(object):

    def __init__(self, domain):
        self.loadCredentials(domain)


    def setUser(self, username):
        self._username = username

    def setPassword(self, password):
        self._password = password

    def getUser(self):
        return self._username

    def getPassword(self):
        return self._password

    def loadCredentials(self, domain):
        home = os.getenv("HOME")
        auth_file = os.path.join(home,"Documents/Authentications/Scrapers.json")
        print(auth_file)
        with open(auth_file,'r') as json_file:
            json_data = json.load(json_file)

        try:
            domain_credentials = json_data[domain]
            self._username = domain_credentials["User"]
            self._password = domain_credentials["Pass"]
        except KeyError:
            print("Domain does not exsist in authe file.")





class RoboProcess(Executor):

    def __init__(self):
        Executor.__init__(self)
        chromedriver = "/home/andrew/Projects/03_Pinscraper/webdrivers/chromedriver"
        self._driver = webdriver.Chrome(executable_path=chromedriver)
        #todo declare Curator
        self._Curator = Curator("pinterest")
        #todo data and solvers
        #data should be a class every appended object
        #parent access, make a new class that inherits data
        self._data = [self._driver, self._Curator]


    def __call__(self):
        Executor.__call__(self, self._driver)

def WebScraper():
    chromedriver = "/home/andrew/Projects/03_Pinscraper/webdrivers/chromedriver"
    return webdriver.Chrome(executable_path=chromedriver)






def main():


    LoginInfo = User("Pinterest")

    Scraper = ObjectMaker.makeObject()

    crawlerData = Data("Driver", WebScraper())
    curatorData = Data("Curator", Curator("pinterest"))

    Scraper.addData(crawlerData)
    Scraper.addData(curatorData)

    print(Scraper)




    Nav = Navigator(url="https://www.pinterest.com/pin/AZQF9zkJ2bC5GQuxb8T0EWKZvhuTecFBgOMfPOk5YMigVsLmdBA0EY4/")
    #print(Nav)
    Scraper.add(Nav)
    Scraper()
    #rb = RoboProcess()

    #rb.add(Nav)
    #rb.add(PinterestLogin(LoginInfo))

    #rb.add(PinSaver())
    #rb.add(BoardCollector())
    #rb.add(PinCollector())

    #add sub rb process /sequential cumulative process?

    #collect up related pins

    #go to src website and scrape

    #build neural net to recognize images

    #build recurrent network to scrape

    #build generative advisarial network







    #rb()


main()











