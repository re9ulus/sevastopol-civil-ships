from area import Area
from coordinates import Coordinates
from coordinates import Angle


p = [Coordinates(0,0), Coordinates(0,2), Coordinates(2,2), Coordinates(2,0)]
x = Coordinates(1,1)
f = Area(p)
f.__start_point__()
print f.__das_is_in__(x)
