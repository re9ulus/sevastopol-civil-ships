from coordinates import Coordinates
#from coordinates import Angle

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)

# Перечисления положений
# Внутри, Снаружи, На границе
polygon_position = enum('INSIDE', 'OUTSIDE', 'BOUNDARY')
# Касается, Пересекает, Не имеет значения
edge_position = enum('TOUCHING', 'CROSSING', 'INESSENTIAL')
# Слева, Справа, Впереди, Сзади, Между, В начале, В конце
point_position = enum('LEFT',  'RIGHT',  'BEYOND',  'BEHIND', 'BETWEEN', 'ORIGIN', 'DESTINATION')


class Area:
    '''
    Area class.
    '''
    def __init__(self, points) :
        self.points = points
        self.zero = points[0]
        
    def __start_point__ (self) :
        '''
        Перегрупировывает точки многоугольника для обхода по часовой стрелки слева снизу
        '''
        # указатель на начальную точку обхода
        zero_id = 0 
        for i in range(len(self.points)) :
            if (self.points[i].latitude < self.points[zero_id].latitude) or ( (self.points[i].latitude == self.points[zero_id].latitude) and (self.points[i].longitude < self.points[zero_id].longitude) ) :
                zero_id = i

        self.zero = self.points[zero_id]
        self.points = self.points[zero_id:] + self.points[:zero_id]

    def __das_is_in__(self, point) :
        '''
        Приобразовувает к читабельному виду
        '''
        return polygon_position.reverse_mapping[self.__point_in_polygon__(point)]

    def __point_in_polygon__(self, point) :
        '''
        Определяет принадлежность точки многоугольнику
        '''
        is_in = False
        for i in range(len(self.points)) :
            if (i == len(self.points) - 1) :
                #print ";)", len(self.points)
                edge = self.points[i], self.points[0]
            else :
                #print ":("
                edge = self.points[i], self.points[i+1]

            foo = self.__edge_type__(point, edge)
            if (foo == edge_position.TOUCHING) :
                #print(i, edge[0].latitude, edge[0].longitude, edge[1].latitude, edge[1].longitude)
                return polygon_position.BOUNDARY
            elif (foo == edge_position.CROSSING) :
                is_in = not is_in

        return [polygon_position.OUTSIDE, polygon_position.INSIDE] [is_in]

    def __edge_type__(self, point, edge):
        '''
        Определяет каким по отношению к точке является реборо
        '''
        start, end = edge 
        pos = self.__classify__(point, start, end)
        #print point_position.reverse_mapping[pos]

        if (pos == point_position.LEFT) :
            return [edge_position.INESSENTIAL, edge_position.CROSSING] [(start.longitude < point.longitude) and (point.longitude <= end.longitude)]
    
        if (pos == point_position.RIGHT) :
            return [edge_position.INESSENTIAL, edge_position.CROSSING] [(end.longitude < point.longitude) and (point.longitude <= start.longitude)]

        if (pos == point_position.BETWEEN) or (pos == point_position.ORIGIN) or (pos == point_position.DESTINATION) :
            return edge_position.TOUCHING

        return edge_position.INESSENTIAL

    def __classify__ (self, point, start, end) :
        a = end - start
        b = point - start
        sa = a.latitude * b.longitude - b.latitude * a.longitude
        #print a.latitude, a.longitude, b.latitude, b.longitude, sa

        if (sa > 0.0) :
            return point_position.LEFT
        elif (sa < 0.0) :
            return point_position.RIGHT

        if (a.latitude * b.latitude < 0.0) or (a.longitude * b.longitude < 0.0) :
            return point_position.BEHIND

        if (a.length() < b.length()):
            return point_position.BEYOND

        if (start == point):
            return point_position.ORIGIN

        if (end == point):
            return point_position.DESTINATION

        return point_position.BETWEEN
