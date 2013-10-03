from src.coordinates import Coordinates
#from math import *
from src.ship import Ship
from src.area import Area
from src.kmlparser import KmlParser
from src.route import Route
from src.pier import Pier
from src.scrapper import Scrapper 
from src.magic_numbers import MN

import time

Kml = KmlParser()

routes = [
Route(Kml.parse("Bay\\Gorod - Severnaja.kml")),
Route(Kml.parse("Bay\\Artbuhta - Severnaja.kml")),
Route(Kml.parse("Bay\\Artbuhta - Radiogorka.kml"))
]

caters = ["WEST", "ORION", "G. OVCHINNIKOV", "ZUYD",
 "PERSEY", "OST", "URAN", "MOLODIZGNIY", "SATURN", "MERKURIY",
 "ADMIRAL LAZAREV", "ADMIRAL ISTOMIN", "V ADMIRAL KLOKACHEV",
 "NORD"]

#print caters

scr = Scrapper()
#scr = scr.scrape_all_ships(scr)

Caters = []
for c in caters:
	Caters.append(Ship(c))

A1 = Pier(Kml.parse_pier("Bay\\Grafskaja pristan.kml"));
A2 = Pier(Kml.parse_pier("Bay\\Severnaja kater.kml"));
B1 = Pier(Kml.parse_pier("Bay\\Art buhta parom.kml"));
B2 = Pier(Kml.parse_pier("Bay\\Severnaja parom.kml"));
C1 = Pier(Kml.parse_pier("Bay\\Art buhta kater.kml"));
C2 = Pier(Kml.parse_pier("Bay\\Radiogorka.kml"));

routes[0].piers = [A1, A2]
routes[1].piers = [B1, B2]
routes[2].piers = [C1, C2]

#print grafskaya
#print nordside

data = scr.scrape_all_ships(caters)

def printpos():
	for cater in Caters:
		if (cater.ais_status() == "ONLINE") and (cater.route != -1) :
			route = routes[cater.route]
			if (cater.speed < MN.STOP):
				print cater.name, ": stay  at :", route.destination(cater).name
			else:
				print cater.name, ": route to :", route.destination(cater).name

def whatroute():
	for cater in Caters:
		if (cater.ais_status() == "ONLINE") :
			counter = []
			for route in routes:
				counter.append(route.verification(cater))
			maxpos = max(counter)
			if maxpos :
				cater.route = counter.index(maxpos)
			else :
				cater.route = -1

def upd():
	data = scr.scrape_all_ships(caters)
	for cater in Caters :
		if cater.name in data:
			cater.update(data[cater.name])
		else:
			cater.update(None)

print "----------------------------------"
timer = 35
for t in range(timer):
	upd()
	whatroute()
	printpos()

	print "----------------------------------"
	print "I am still work {0} minute remain".format(5 * (timer-t) )
	print "----------------------------------"
	time.sleep (2 * 60) #2 min delay