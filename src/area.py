from coordinates import Coordinates
from coordinates import Angle

class Area:
    '''
    Area class.
    '''
    def __init__(self, points) :
        self.points = points
        self.angles = []
        self.zero = points[0]
        
    def __start_point__ (self) :
    '''
    Перегрупировывает точки многоугольника для обхода по часовой стрелки слева снизу
    '''
    # указатель на начальную точку обхода
    zero_id = 0 
    for i in range(len(self.points)):
        if (self.points[i].latitude < self.points[zero_id].latitude) or (self.points[i].latitude == points[zero_id].latitude) and (points[i].longitude < points[zero_id].longitude) :
            zero_id = i

    zero = points[zero_id]
    points = points[zero_id+1:] + points[:zero_id]
    for i in range(len(self.points)) :
                    angles[i].fst = points[i].longitude - zero.longitude
                    angles[i].scd = points[i].latitude - zero.latitude
                    if (angles[i].fst == 0) :
                        angles[i].scd = [1, -1] [angles[i].scd < 0]
    
    def __das_is_in__ (point) :
    '''
    Определяет принадленжность точки
    '''
    is_in = False
    if (point.latitude >= zero.latitude) :
        if (point.latitude == zero.latitude) and (point.longitude == zero.longitude) :
            is_in = True
        else :
            angle.fst = point.longitude-zero.longitude
            angle.scd = point.latitude-zero.latitude
            if (angle.fst == 0):
                angle.scd = [1, -1] [angle.scd    < 0]    
            
            flag = False
            for it in angles:
                if (it > angle):
                    flag = True
                    break
            
            if (not flag) and (angle == angles[-1]):
                    it = angles[-1]
            if (flag) and (it != angles[0]) :
                    pt = angles.index(it)
                    if (Coordinates.__square__(points[pt], points[pt-1], point) <= 0) :
                        is_in = true            
    return ["OUTSIDE", "INSIDE"] [is_in]
