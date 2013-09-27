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

    def scrape_ship(self, ship_name):
        '''
        Scrape ship data from AIS.
        return: ( speed, course, (latitude, longitude) )
        '''
<<<<<<< HEAD
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
=======
        url = r"http://www.marinetraffic.com/ais/datasheet.aspx?datasource=SHIPS_CURRENT&PORT_ID=883&SHIPNAME={0}".format(ship_name)
        try:
            soup = BeautifulSoup(urllib2.urlopen(url).read())
            data = soup.find("a",class_='data',text=ship_name).find_parent("tr").find_all("td")
            speed = float(data[3].text)
            course = float(data[4].text)
            raw_position = data[9].find("a")["href"]
            pattern = re.compile(r"centerx=([0-9\.]+)&centery=([0-9\.]+)")
            m = pattern.search(raw_position)
            longitude = float(m.group(1))
            latitude = float(m.group(2))
            res = ( speed, course, (latitude, longitude) )
        except (AttributeError, urllib2.URLError):
            res = None
        finally:
            return res
>>>>>>> 891949d9b44f1bc4b44c7ec3913490f8c8af0136
