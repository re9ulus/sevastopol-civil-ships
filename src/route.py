from area import Area
from pier import Pier
from ship import Ship
from magic_numbers import MN

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

    def verification(self, ship) :
        '''
        Checks Is the ship on the route
        '''
        if not self.bay.is_inside(ship.coordinates):
            return 0
        else:
            count = 1

        if (ship.speed < MN.STOP):
            for pier in self.piers:
                if pier.area.is_inside(ship.coordinates):
                    return MN.TRUEPOS

        for point in ship.lastpos:
            count += self.bay.is_inside(point)

        return count

    def destination(self, ship) :
        '''
        Returns pier destination route
        '''
        if not self.bay.is_inside(ship.coordinates):
            return None

        if (ship.speed < MN.STOP):
            for pier in self.piers:
                if pier.area.is_inside(ship.coordinates):
                    return pier

        angle = MN.MAX
        res = None

        for pier in self.piers:
            foo = ship.angle(pier.mark)
            if foo < angle:
                angle = foo
                res = pier

        return res