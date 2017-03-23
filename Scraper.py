from selenium import webdriver
from ProcessFactory import Processor
from ScryEngine.microscrapers.general import Navigator
from ScryEngine.microscrapers.pinterest import PinterestLogin
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




class RoboProcess(Processor):

    def __init__(self):
        Processor.__init__(self)
        chromedriver = "/home/andrew/Projects/03_Pinscraper/webdrivers/chromedriver"
        self._driver = webdriver.Chrome(executable_path=chromedriver)


    def run(self):
        Processor.run(self, self._driver)




def main():

    #todo: Load credentials to a local file and load them in with client obj
    LoginInfo = User()
    LoginInfo.setUser("amelnychukoseen@gmail.com")
    LoginInfo.setPassword("NoPass")

    Nav = Navigator(url="https://www.pinterest.com/pin/AZQF9zkJ2bC5GQuxb8T0EWKZvhuTecFBgOMfPOk5YMigVsLmdBA0EY4/")
    print(Nav)
    rb = RoboProcess()

    rb.add(Nav)
    rb.add(PinterestLogin(LoginInfo))
    #todo add complex scraper behaviour
    #todo test recusive scraper behaviour


    rb.run()


main()











