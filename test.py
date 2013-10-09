from area import Area
from coordinates import Coordinates

print "----"
print "|  |"
print "----"

p = [Coordinates(0,0), Coordinates(0,2), Coordinates(2,2), Coordinates(2,0)]
x = [Coordinates(0,0), Coordinates(0,1), Coordinates(0.5,2), Coordinates(1,1), Coordinates(2,0.5), Coordinates(2,3), Coordinates(-10,1)]
f = Area(p)
f.__start_point__()
for i in x:
    print i.latitude, i.longitude, f.__das_is_in__(i)

print "---------------------"

print "|\/|"
print "----"

p = [Coordinates(0,0), Coordinates(0,2), Coordinates(2,0), Coordinates(4,2), Coordinates(4,0)]
x = [Coordinates(0,0), Coordinates(0,1), Coordinates(0.5,2), Coordinates(1,1), Coordinates(2,0.5), Coordinates(2,3), Coordinates(-10,1)]
f = Area(p)
f.__start_point__()
for i in x:
    print i.latitude, i.longitude, f.__das_is_in__(i)
