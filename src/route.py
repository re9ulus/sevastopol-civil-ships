from area import Area
from pier import Pier

class Route:
    '''
    A Route class
    '''
    def __init__(self, name, bay=None, piers=None) :
        self.name = name
        self.bay = bay
        self.piers = piers

    def __init__(self, parser, piers=None) :
        '''
        Parser (str, Area)
        '''
        self.name = parser[0]
        self.bay = parser[1]
        self.piers = piers

    def __str__(self):
        return "route: {0};".format(self.name)