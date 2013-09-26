class Coordinates:
  '''
  Coordinates class.
  '''
  def __init__(self,latitude,longitude):
    self.latitude = latitude
    self.longitude = longitude

  def __square__ (a, b, c):
    return a.latitude*(b.longitude-c.longitude) + b.latitude*(c.longitude-a.longitude) + c.latitude*(a.longitude-b.longitude)

class Angle:
  '''
  Angle class.
  '''
  def __init__(self, fst, scd):
    self.fst = fst
    self.scd = scd  
  
  def __lt__ (self, point):
    if (self.scd == 0) and (point.scd == 0) :
      return (self.fst < point.fst)
    return ((self.fst * point.scd) < (self.scd * point.fst))