class Coordinates:
  '''
  Coordinates class.
  '''
  def __init__(self,latitude,longitude):
    self.latitude = latitude
    self.longitude = longitude

  def __square__ (a, b, c)
	return a.latitude*(b.longitude-c.longitude) + b.latitude*(c.longitude-a.longitude) + c.latitude*(a.longitude-b.longitude)

class Angle
  '''
  Angle class.
  '''
  def __init__(self, rho, phi):
    self.rho = rho
    self.phi = phi  
  
  def __lt__ (self, point)
    if (self.phi == 0) and (point.phi == 0) :
		return (self.rho < point.rho)
	return (self.rho * point.phi) < (self.phi * point.rho)
 	