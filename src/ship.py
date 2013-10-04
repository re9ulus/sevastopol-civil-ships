from coordinates import Coordinates
from scrapper import Scrapper
from enum import Enum
from magic_numbers import MN

ship_status = Enum("ONLINE", "OFFLINE")

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
<<<<<<< HEAD
        self.lastpierindex = None
=======
>>>>>>> 43a22185c5f478b4129b368fea5c994dad70685c
        self.route = None

    def update(self, data):
        if data:
            if (self.coordinates) and (self.speed > MN.STOP) :
<<<<<<< HEAD
                if not (self.lastpos.count(self.coordinates)) :
                    self.lastpos.append(self.coordinates)

            if len(self.lastpos)>MN.LASTPOSLEN:
                self.lastpos.pop(0)# = self.lastpos[-MN.LASTPOSLEN:]
=======
                self.lastpos.append(self.coordinates)
            if len(self.lastpos)>MN.LASTPOSLEN:
                self.lastpos = self.lastpos[-MN.LASTPOSLEN:]
>>>>>>> 43a22185c5f478b4129b368fea5c994dad70685c

            self.speed = data[0]
            self.course = data[1]
            self.coordinates = Coordinates(data[2][0], data[2][1])
            self.status = ship_status.ONLINE
        else:
            self.status = ship_status.OFFLINE

    def update_from_ais(self):
        scrapper = Scrapper()
        data = scrapper.scrape_ship(self.name)
        self.update(data)

    def __str__(self):
        if self.status == ship_status.ONLINE:
            res = "name: {0}; speed: {1}; course: {2}; coordinates: {3}; route: {4};".format(self.name, self.speed, self.course, self.coordinates, self.route)
        else:
            res = "name: {0} Not Found".format(self.name)
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
