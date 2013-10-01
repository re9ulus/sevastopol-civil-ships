from src.scrapper import Scrapper
from src.ship import Ship
from src.area import Area
from src.coordinates import Coordinates
from src.kmlparser import KmlParser
from src.route import Route
import time

Kml = KmlParser()

#Route(Kml.parse("Bay\\City-Nord.kml"))
routes = [Route(Kml.parse("Bay\\City-Nord.kml")), Route(Kml.parse("Bay\\Art-Nord.kml")), Route(Kml.parse("Bay\\Art-Rad.kml")) ]

caters = ["WEST", "URAN", "MERKURIY", "OST",
 "ORION", "G. OVCHINNIKOV", "ZUYD", "PERSEY",
 "MOLODIZGNIY", "ADMIRAL LAZAREV", "SATURN",
 "ADMIRAL ISTOMIN", "V ADMIRAL KLOKACHEV", "NORD"]
 
Caters = []
for c in caters:
	Caters.append(Ship(c))

#for cater in Caters :
#	cater.update_from_ais()
#	if (cater.ais_status() == "ONLINE") :
#		print cater
#	else:
#		print cater.name, "Not FOUND"

timer = 5
for t in range(timer):
	for cater in Caters :
		#res = Scrap.scrape_ship(cater.name)
		cater.update_from_ais()
		#if len(cater.lastpos) == 5:
		if (cater.ais_status() == "ONLINE") :
			counter = []
			for route in routes:
				counter.append(0)
				if (route.bay.is_inside(cater.coordinates)):
					counter[-1] += 1				
				for pos in cater.lastpos :
					if (route.bay.is_inside(pos)):
						counter[-1] += 1
			maxpos = max(counter)
			if maxpos :
				cater.route = routes[counter.index(maxpos)].name
			else :
				cater.route = "Outsider"

	#print "I am still work {0} minute remain".format(5 * (timer-t) )
	#time.sleep (5 * 60) #5 min delay

for cater in Caters:
	if (cater.ais_status() == "ONLINE") :
		print "name: ", cater.name, "route: ", cater.route
	else:
		print "name: ", cater.name, " ! Not FOUND !"