from coordinates import Coordinates
from scrapper import Scrapper
from enum import Enum
from magic_numbers import MN

ship_status = Enum("ONLINE", "OFFLINE", "INDEADEND")

class Ship:
    '''
    A Ship class
    '''
    def __init__(self, name, speed=None, course=None, coordinates=None):
        # TODO: Add last_update time
        if isinstance(name, list):
            self.name = name[0]
            self.nick = unicode(name[1], "UTF-8")[:-1] # \n Kill
        else:
            self.name = self.nick = name

        self.coordinates = coordinates
        self.speed = speed
        self.status = ship_status.OFFLINE
        
        self.lastpos = []
        self.lastpierindex = None
        self.route = None

    def reset(self):
        #self.coordinates = None
        #self.course = None
        #self.speed = None       
        
        self.lastpos = []
        self.lastpierindex = None
        self.route = None
        
        #self.status = ship_status.OFFLINE

    def update(self, data):
        if data:
            if (self.coordinates) and (self.speed > MN.STOP) :
                if not (self.lastpos.count(self.coordinates)) :
                    self.lastpos.append(self.coordinates)

            if len(self.lastpos)>MN.LASTPOSLEN:
                self.lastpos.pop(0)# = self.lastpos[-MN.LASTPOSLEN:]

            self.speed = data[0]
            self.course = data[1]
            self.coordinates = Coordinates(data[2][0], data[2][1])
            self.status = ship_status.ONLINE
        else:
            self.reset()
            status = ship_status.OFFLINE

    def update_from_ais(self):
        scrapper = Scrapper()
        data = scrapper.scrape_ship(self.name)
        self.update(data)

    def __str__(self):
        if self.status == ship_status.ONLINE:
            res = "name: {0}; speed: {1}; course: {2}; coordinates: {3}; route: {4};".format(self.name, self.speed, self.course, self.coordinates, self.route)
        else:
            res = "name: {0}; ais status: {1}".format(self.name, self.ais_status())
        return res


    def ais_status(self):
        return ship_status.reverse_mapping[self.status]

    def angle (self, point):
        '''
        Easy use for Coordinates.angle()
        '''
        return self.coordinates.angle(self.course, point)

    def viewangle(self, point):
        return self.angle(point) < MN.VIEWANGLE

    def deadend(self, zone):
        if self.status == ship_status.OFFLINE:
            return False

        if (zone.area.is_inside(self.coordinates)):
            if (self.speed < MN.STOP) or (self.viewangle(zone.mark)):
                self.status = ship_status.INDEADEND
                self.reset()
                return True

        return False