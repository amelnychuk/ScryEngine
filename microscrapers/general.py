import time



from Executor import Executor




class Navigator(Executor):

    #todo: add data requirements, these will inherit from Operator/Solver

    def __init__(self, url=""):
        Executor.__init__(self)
        self.seturl(url)
        #print(self.__class__.getDriver())
        #print(self.getDriver())


    def seturl(self, url):
        self._url = url

    @Executor.task
    def get(self):
        print("Navigating")
        print("data:", self._data)
        print("classdata:", self.getData())
        driver = self.getDriver()
        driver.get(self._url)
        time.sleep(.1)



class Scrollers(Executor):

    @Executor.task
    def vertScroll(self, driver):
        prev_scrollHeight = 99999
        counter = 0
        while prev_scrollHeight != driver.execute_script("return window.pageYOffset;") and counter < 3:
            prev_scrollHeight = driver.execute_script("return window.pageYOffset;")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            counter += 1