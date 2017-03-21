from selenium import webdriver
import ProcessFactory
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


class RoboProcess(ProcessFactory.Processor):

    def __init__(self):

        chromedriver = "/home/andrew/Projects/03_Pinscraper/webdrivers/chromedriver"
        self._driver = webdriver.Chrome(executable_path=chromedriver)








