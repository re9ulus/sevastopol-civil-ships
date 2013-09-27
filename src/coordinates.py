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

    def length(self):
        '''
        Определяет длину вектора заданного координатами
        '''
        from math import sqrt
        return sqrt(self.latitude*self.latitude + self.longitude*self.longitude)

    def __str__(self):
        return "latitude: {0}; longitude: {1}".format(self.latitude, self.longitude) 

#class Angle:
#  '''
#  Angle class.
#  '''
#  def __init__(self, fst, scd):
#    self.fst = fst
#    self.scd = scd  
#  
#  def __lt__ (self, point):
#    if (self.scd == 0) and (point.scd == 0) :
#      return (self.fst < point.fst)
#    return ((self.fst * point.scd) < (self.scd * point.fst))