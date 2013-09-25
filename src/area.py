from coordinates import Coordinates
from coordinates import Angle

class Area:
  '''
  Area class.
  '''
  def __init__(self, points []):
    self.points = points
    self.angles = []
	self.zero = points[0]
	
  def __start_point__ () :
	'''
	Перегрупировывает точки многоугольника для обхода по часовой стрелки слева снизу
	'''
  	zero_id = 0 # указатель на начальную точку обхода
	for i in range(len(self.points)) :
		if (points[i].latitude < points[zero_id].latitude) or (points[i].latitude == points[zero_id].latitude) and (points[i].longitude < points[zero_id].longitude) :
			zero_id = i

	zero = points[zero_id]
	## warning 	rotate (p.begin(), p.begin()+zero_id, p.end()); p.erase (p.begin());
	points = points[zero_id+1:] + points[:zero_id]	## Кажется правильно делаю? поменять порядок элементов и кильнуть первый?
	for i in range(len(self.points)) :
		angles[i].rho = points[i].longitude - zero.longitude
		angles[i].phi = points[i].latitude - zero.latitude
			if (angles[i].rho == 0) :
				angles[i].phi = [1, -1] [angles[i].phi < 0]
  
  def __das_is_in__ (point) 
    '''
	Определяет принадленжность точки
	'''
	is_in = False
	if (point.latitude >= zero.latitude) :
		if (point.latitude == zero.latitude) and (point.longitude == zero.longitude) :
			is_in = True
		else :
			angle.rho = point.longitude-zero.longitude
			angle.phi = point.latitude-zero.latitude
			if (angle.rho == 0):
				angle.phi = [1, -1] [angle.phi  < 0]	
			
			vector<ang>::iterator it = upper_bound (a.begin(), a.end(), my);
			if (it == a.end() && my.a == a[n-1].a && my.b == a[n-1].b)
				it = a.end()-1;
			if (it != a.end() && it != a.begin()) {
				int p1 = int (it - a.begin());
				if (sq (p[p1], p[p1-1], q) <= 0)
					in = true;
	return ["OUTSIDE", "INSIDE"] [is_in]