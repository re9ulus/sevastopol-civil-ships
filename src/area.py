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
            if (self.points[i].latitude < self.points[zero_id].latitude) or ( (self.points[i].latitude == self.points[zero_id].latitude) and (self.points[i].longitude < self.points[zero_id].longitude) ) :
                zero_id = i

        self.zero = self.points[zero_id]
        self.points = self.points[zero_id+1:] + self.points[:zero_id]
        for i in range(len(self.points)) :
                        self.angles.append(Angle(self.points[i].longitude - self.zero.longitude, self.points[i].latitude - self.zero.latitude))
                        if (self.angles[i].fst == 0) :
                            self.angles[i].scd = [1, -1] [self.angles[i].scd < 0]
        
    def __das_is_in__ (self, point) :
        '''
        Определяет принадленжность точки
        '''
        is_in = False
        if (point.latitude >= self.zero.latitude) :
            if (point.latitude == self.zero.latitude) and (point.longitude == self.zero.longitude) :
                is_in = True
            else :
                angle = Angle(point.longitude-self.zero.longitude, point.latitude-self.zero.latitude)
                if (angle.fst == 0):
                    angle.scd = [1, -1] [angle.scd < 0]
                
                flag = False
                for it in self.angles:
                    if (it > angle):
                        flag = True
                        break

                if (not flag) and (angle == self.angles[-1]) :
                    it = angles[-1]

                if (flag) and (it != self.angles[0]) :
                    pt = self.angles.index(it)
                    print(pt)
                if (Coordinates.__square__(self.points[pt], self.points[pt-1], point) <= 0) :
                    is_in = True      
							
        return ["OUTSIDE", "INSIDE"] [is_in]
