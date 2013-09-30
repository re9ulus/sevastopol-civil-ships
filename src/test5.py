from coordinates import Coordinates
#from math import *
from ship import Ship
from area import Area
from kmlparser import KmlParser
from route import Route

Kml = KmlParser()

routes = [Route("City-Nord", Kml.parse("Bay\\City-Nord.kml"))]#, Route("Art-Nord", Kml.parse("Bay\\Art-Nord.kml")), Route("Art-Rad", Kml.parse("Bay\\Art-Rad.kml")) ]

#start = Coordinates(0,0)
#dest = Coordinates(0,10)

#for i in range (360/5):
#	print 5 * i, start.angle(5 * i, dest), (360 + 90 - 5 * i)*pi/180


caters = ["MERKURIY", "OST", "ORION", "G. OVCHINNIKOV", "ZUYD", "PERSEY", "MOLODIZGNIY", "ADMIRAL LAZAREV", "SATURN", "ADMIRAL ISTOMIN", "V ADMIRAL KLOKACHEV", "NORD"]
Caters = []
for c in caters:
	Caters.append(Ship(c))

Citi = Coordinates (44.592388, 33.515543)
Nord = Coordinates (44.638450, 33.546545)
#Rad = Coordinates (44.628540, 33.524681)
#Art = Coordinates (44.613110, 33.518858)


for cater in Caters:
	cater.update_from_ais()
	if (cater.ais_status() == "ONLINE") :
		#if (routes[0].bay.is_inside(cater.coordinates)) :
		#print cater.coordinates.angle(cater.course, Citi)
		#print cater.coordinates.angle(cater.course, Nord)
		#print cater.course
		#print
			#if (cater.coordinates.angle(cater.course, Citi) < cater.coordinates.angle(cater.course, Nord) ):
		if (cater.angle(Citi) < cater.angle(Nord) ):
			print "name: ", cater.name, "route: to City", cater.course
		else:
			print "name: ", cater.name, "route: to Nord", cater.course
#		else:
#			print "name: ", cater.name, " ! Outsider !"
#	else:
#		print "name: ", cater.name, " ! Not FOUND !"