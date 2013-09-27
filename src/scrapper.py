import urllib2
from bs4 import BeautifulSoup
import re

from coordinates import Coordinates

class Scrapper:
    '''
    Scrapper class.
    '''
    def __init__(self):
        pass

    def scrape_ship(self, ship_name, ship_type="Passenger", city="SEVASTOPOL"):
        '''
        Scrape ship data from AIS.
        return: ( speed, course, (latitude, longitude) )
        '''
        url = r"http://www.marinetraffic.com/ais/datasheet.aspx?SHIPNAME={0}&TYPE_SUMMARY={1}&menuid=&datasource=SHIPS_CURRENT&app=&mode=&B1=Search".format(ship_name, ship_type)
        soup = BeautifulSoup(urllib2.urlopen(url).read())
        data = soup.find("a",class_='data',text=city).find_parent("tr").find_all("td")
        speed = float(data[3].text)
        course = float(data[4].text)
        raw_position = data[7].find("a")["href"]
        pattern = re.compile(r"centerx=([0-9\.]+)&centery=([0-9\.]+)")
        m = pattern.search(raw_position)
        longitude = float(m.group(1))
        latitude = float(m.group(2))
        return speed, course, Coordinates(latitude, longitude)