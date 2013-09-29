from coordinates import Coordinates
from scrapper import Scrapper
from enum import Enum

ship_status = Enum("ONLINE", "OFLINE")

class Ship:
    '''
    A Ship class
    '''
    def __init__(self, name, speed=None, course=None, coordinates=None):
        # TODO: Add last_update time
        self.name = name
        self.coordinates = coordinates
        self.speed = speed
        self.status = ship_status.OFLINE
        
        self.lastpos = []
        self.route = ""

    def update_from_ais(self):
        scrapper = Scrapper()
        data = scrapper.scrape_ship(self.name)
        if data:
            if self.coordinates:
                self.lastpos.append(self.coordinates)
            if len(self.lastpos)>10:
                self.lastpos = self.lastpos[-10:]

            self.speed = data[0]
            self.course = data[1]
            self.coordinates = Coordinates(data[2][0], data[2][1])
            self.status = ship_status.ONLINE
        else:
            self.status = ship_status.OFLINE


    def __str__(self):
        return "name: {0}; speed: {1}; course: {2}; coordinates: {3}; route: {4};".format(self.name, self.speed, self.course, self.coordinates, self.route)

    def ais_status(self):
        return ship_status.reverse_mapping[self.status]
