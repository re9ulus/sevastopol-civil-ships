from math import *

class Coordinates:
    '''
    Coordinates class.
    '''
    def __init__(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude

    def square (a, b, c):
        return a.latitude*(b.longitude-c.longitude) + b.latitude*(c.longitude-a.longitude) + c.latitude*(a.longitude-b.longitude)

    def __sub__ (self, point):
        return Coordinates(self.latitude - point.latitude, self.longitude - point.longitude)

    def __add__ (self, point):
        return Coordinates(self.latitude + point.latitude, self.longitude + point.longitude)

    def __mul__ (self, point):
        return self.latitude * point.latitude + self.longitude * point.longitude

    def __lt__ (self, point):
        return (self.latitude < point.latitude) or ( (self.latitude == point.latitude) and (self.longitude < point.longitude) ) 

    def __eq__ (self, point):
        return (self.latitude == point.latitude) and (self.longitude == point.longitude)

    def __ne__ (self, point):
        return not (self == point)

    def length(self):
        '''
        Определяет длину вектора заданного координатами
        '''
        return sqrt(self.latitude * self.latitude + self.longitude * self.longitude)

    def __str__(self):
        return "latitude: {0}; longitude: {1}".format(self.latitude, self.longitude) 

# -------------------------------------------------
# NED DEBUG
# Latitude == Y
# Longitude == X

    def angle(self, course, dest):
        '''
        Calculates the angle between the vectors
        from the point "self" to the point "dest"
        and from the point of "self" with angle "course"
        '''
        #phi = cours to radian Decart angle
        phi = (450 - course) % 360 #grad
        #print phi
        phi = pi * phi / 180 #rad

        A = Coordinates(sin(phi), cos(phi))
        B = dest - self

        scalar = A * B / ( A.length() * B.length() )
        
        co = acos(scalar) / pi * 180
        #print co
        return co #round acos(scalar)

    def collinear(self, course, start):
        '''
        Return bool is a vectors are collinear
        '''
        phi = (450 - course) % 360 #grad
        phi = pi * phi / 180 #rad

        A = Coordinates(sin(phi), cos(phi))
        B = self - start
        scalar = A * B / ( A.length() * B.length() )

        return scalar > 0
# ---------------------------------------------------