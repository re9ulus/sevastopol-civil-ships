import urllib2
from bs4 import BeautifulSoup
import codecs

class Scrapper:
    '''
    Scrapper class.
    '''
    def __init__(self, ais_url = 'http://www.marinetraffic.com/'):
        pass

    def scrapeShip(self, ship_name, ship_type="Passenger"):
        #url = "http://www.marinetraffic.com/ais/ru/datasheet.aspx?SHIPNAME={0}&TYPE_SUMMARY={1}&menuid=&datasource=SHIPS_CURRENT&app=&mode=&B1=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA".format(ship_name, ship_type)
        url = r"http://www.marinetraffic.com/ais/datasheet.aspx?SHIPNAME=NORD&TYPE_SUMMARY=Passenger&menuid=&datasource=SHIPS_CURRENT&app=&mode=&B1=Search"
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html)
        print soup.find("a",class_='data',text="SEVASTOPOL").find_parent("tr")
        # TODO: parse table row

scrapper = Scrapper()

scrapper.scrapeShip('NORD')