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
<<<<<<< HEAD
            x = [0, ship.lastpierindex] [ship.lastpierindex != None]
            for i in range(len(self.piers)):
                pier = self.piers[(x + i) % len(self.piers)]
                if pier.area.is_inside(ship.coordinates):
                    ship.lastpierindex = (x + i) % len(self.piers)
                    return pier

        if (ship.lastpierindex != None):
            if ship.viewangle(self.piers[(ship.lastpierindex + 1) % len(self.piers)].mark):
                return self.piers[(ship.lastpierindex + 1) % len(self.piers)]
            elif ship.viewangle(self.piers[(len(self.piers) + ship.lastpierindex - 1) % len(self.piers)].mark):
                return self.piers[ (len(self.piers) + ship.lastpierindex - 1) % len(self.piers)]
            else:
                return self.piers[(ship.lastpierindex + 1) % len(self.piers)]

=======
            for pier in self.piers:
                if pier.area.is_inside(ship.coordinates):
                    return pier

>>>>>>> 43a22185c5f478b4129b368fea5c994dad70685c
        angle = MN.MAX
        res = None

        for pier in self.piers:
            foo = ship.angle(pier.mark)
            if foo < angle:
                angle = foo
                res = pier

        return res