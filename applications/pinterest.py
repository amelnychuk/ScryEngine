from credentials.domains import PinterestClient
from microscrapers.general import Navigator, Scrollers
from microscrapers.pinterest import PinterestLogin

from Scraper import RoboBrowser, MicroScraper, MacroScraper




def pinscraper(url):
    Scraper = MacroScraper()
    Scraper.add(Navigator(url=url))
    Scraper.add(PinterestLogin(PinterestClient()))
    Scraper.add(Scrollers())
    return Scraper


def pinterestCap():


    #Figure out compositing classes for encapsulated options
    rb = RoboBrowser()
    Scraper = Scraper()
    Scraper.add(Navigator(url="https://www.pinterest.com/pin/AZQF9zkJ2bC5GQuxb8T0EWKZvhuTecFBgOMfPOk5YMigVsLmdBA0EY4/"))
    Scraper.add(PinterestLogin(PinterestClient()))
    Scraper.add(scrollers())
    #save image()
    #get pins
    #get boards
    print "Scraper dict: ", Scraper.__dict__
    #Scraper.add(saveDataBase())
    #Scraper()

    rb.add(Scraper)
    rb.scrape()


def nonCapsule():
    rb = RoboBrowser()
    rb.add(Navigator(url="https://www.pinterest.com/pin/AZQF9zkJ2bC5GQuxb8T0EWKZvhuTecFBgOMfPOk5YMigVsLmdBA0EY4/"))
    rb.add(PinterestLogin(PinterestClient()))
    rb.add(Scrollers())
    rb.scrape()

def main():
    pinterestCap()

if __name__ == '__main__':
    rb = RoboBrowser()
    rb.add(pinscraper("https://www.pinterest.com/pin/AZQF9zkJ2bC5GQuxb8T0EWKZvhuTecFBgOMfPOk5YMigVsLmdBA0EY4/"))
    rb
    rb.scrape()