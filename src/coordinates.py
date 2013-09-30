﻿from math import *

class Coordinates:
    '''
    Coordinates class.
    '''
    def __init__(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __square__ (a, b, c):
        return a.latitude*(b.longitude-c.longitude) + b.latitude*(c.longitude-a.longitude) + c.latitude*(a.longitude-b.longitude)

    def __sub__ (self, point):
        return Coordinates(self.latitude - point.latitude, self.longitude - point.longitude)

    def __add__ (self, point):
        return Coordinates(self.latitude + point.latitude, self.longitude + point.longitude)

    def __mul__ (self, point):
        return self.latitude * point.latitude + self.longitude * point.longitude

    def __lt__ (self, point):
        return (self.latitude < point.latitude) or ( (self.latitude == point.latitude) and (self.longitude < point.longitude) ) 

    def length(self):
        '''
        Определяет длину вектора заданного координатами
        '''
        return sqrt(self.latitude*self.latitude + self.longitude*self.longitude)

    def __str__(self):
        return "latitude: {0}; longitude: {1}".format(self.latitude, self.longitude) 

    def angle(self, course, dest):
        '''
        Calculates the angle between the vectors
        from the point "self" to the point "dest"
        and from the point of "self" with angle "course"
        '''
        #phi = cours to radian Decart angle
        #Warning Kostul'
        if (course <= 90):
            phi = 90 - course
        else:
            phi = 450 - course
        #print phi, course
        phi = pi * phi / 180

        A = Coordinates(cos(phi), sin(phi))
        B = dest - self
        scalar = A * B / ( A.length() * B.length() )

        return round( acos(scalar) / pi * 180 )# acos(scalar)#, 

#class Angle:
#  '''
#  Angle class.
#  '''
#  def __init__(self, fst, scd):
#    self.fst = fst
#    self.scd = scd  
#  
