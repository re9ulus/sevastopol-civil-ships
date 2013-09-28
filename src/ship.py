from coordinates import Coordinates
from scrapper import Scrapper

class Ship:
    '''
    A Ship class
    '''
    def __init__(self, name, speed=None, course=None, coordinates=None):
        # TODO: Add last_update time
        self.name = name
        self.coordinates = coordinates
        self.speed = speed

    def update_from_ais(self):
        scrapper = Scrapper()
        data = scrapper.scrape_ship(self.name)
        if data:
            self.speed = data[0]
            self.course = data[1]
            self.coordinates = Coordinates(data[2][0], data[2][1])

    def __str__(self):
        return "name: {0}; speed: {1}; course: {2}; coordinates: {3};".format(self.name, self.speed, self.course, self.coordinates)