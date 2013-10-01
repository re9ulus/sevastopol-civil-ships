from src.coordinates import Coordinates
#from math import *
from src.ship import Ship
from src.area import Area
from src.kmlparser import KmlParser
from src.route import Route
from src.pier import Pier

Kml = KmlParser()

routes = [Route(Kml.parse("Bay\\City-Nord.kml")), Route(Kml.parse("Bay\\Art-Nord.kml")), Route(Kml.parse("Bay\\Art-Rad.kml")) ]

#start = Coordinates(0,0)
#dest = Coordinates(0,10)

#for i in range (360/5):
#	print 5 * i, start.angle(5 * i, dest), (360 + 90 - 5 * i)*pi/180

caters = ["WEST", "ORION",
 "G. OVCHINNIKOV", "ZUYD", "PERSEY", "OST", "URAN",
 "MOLODIZGNIY", "SATURN", "MERKURIY", "ADMIRAL LAZAREV",
 "ADMIRAL ISTOMIN", "V ADMIRAL KLOKACHEV", "NORD"]

#print caters

Caters = []
for c in caters:
	Caters.append(Ship(c))
#	print Caters[-1].name

grafskaya = Pier(Kml.parse_pier("Bay\\Grafskaya-pier.kml"));
nordside = Pier(Kml.parse_pier("Bay\\Nord-pier.kml"));
artbay = Pier(Kml.parse_pier("Bay\\ArtBay-pier.kml"));
raduxa = Pier(Kml.parse_pier("Bay\\RadBay-pier.kml"));

routes[0].piers = [grafskaya, nordside]
routes[1].piers = [artbay, nordside]
routes[2].piers = [artbay, raduxa]

#print grafskaya
#print nordside

for cater in Caters:
	cater.update_from_ais()
	if (cater.ais_status() == "ONLINE") :
		for route in routes:
			if (route.bay.is_inside(cater.coordinates)) :
				if (cater.speed < 0.1):
					for pier in route.piers:
						if (pier.area.is_inside(cater.coordinates)):
							print "name: ", cater.name, "stay", pier.name
				else:
					name = ""
					angle = 999
					for pier in route.piers:
						x = cater.angle(pier.mark)
						if (x < angle):
							angle = x
							name = pier.name
					print "name: ", cater.name, "route to", name #,cater.course
			#else:
			#	print "name: ", cater.name, " ! Outsider !"
	#else:
	#	print "name: ", cater.name, " ! Not FOUND !"