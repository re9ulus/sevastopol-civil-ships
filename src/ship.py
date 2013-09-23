from coordinates import Coordinates

class Ship:
    '''
    A Ship class
    '''
    def __init__(self, name, coordinates, speed):
        self.name = name
        self.coordinates = coordinates
        self.speed = speed

    def __str__(self):
        return "name: {0}; coordinates: {1}; speed: {2}".format(self.name, self.coordinates, self.speed)