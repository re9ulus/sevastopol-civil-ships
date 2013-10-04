from src.coordinates import Coordinates
#from math import *
from src.ship import Ship
from src.area import Area
from src.kmlparser import KmlParser
from src.route import Route
from src.pier import Pier
from src.scrapper import Scrapper 
from src.magic_numbers import MN

<<<<<<< HEAD
from colorama import init
from colorama import Fore, Back, Style
init()

=======
>>>>>>> 43a22185c5f478b4129b368fea5c994dad70685c
import time

Kml = KmlParser()

routes = [
Route(Kml.parse("Bay\\Gorod - Severnaja.kml")),
Route(Kml.parse("Bay\\Artbuhta - Severnaja.kml")),
<<<<<<< HEAD
Route(Kml.parse("Bay\\Artbuhta - Radiogorka.kml")),
Route(Kml.parse("Bay\\Gorod - Gollandija - Inkerman.kml")),
Route(Kml.parse("Bay\\Gorod - Avlita.kml"))
]


caters = []
Caters = []
=======
Route(Kml.parse("Bay\\Artbuhta - Radiogorka.kml"))
]
>>>>>>> 43a22185c5f478b4129b368fea5c994dad70685c

for name in open("ship.list", "r").readlines():
	Caters.append(Ship(name.split("/")))
	caters.append(name.split("/")[0])

#print caters

scr = Scrapper()
#scr = scr.scrape_all_ships(scr)

<<<<<<< HEAD

A1 = Pier(Kml.parse_pier("Bay\\Grafskaja pristan.kml"));
A2 = Pier(Kml.parse_pier("Bay\\Severnaja kater.kml"));

B1 = Pier(Kml.parse_pier("Bay\\Art buhta parom.kml"));
B2 = Pier(Kml.parse_pier("Bay\\Severnaja parom.kml"));

C1 = Pier(Kml.parse_pier("Bay\\Art buhta kater.kml"));
C2 = Pier(Kml.parse_pier("Bay\\Radiogorka.kml"));

D1 = Pier(Kml.parse_pier("Bay\\Pirs u porta.kml"));
D2 = Pier(Kml.parse_pier("Bay\\Somali.kml"));
D3 = Pier(Kml.parse_pier("Bay\\Gollandija.kml"));
D4 = Pier(Kml.parse_pier("Bay\\Ugolnaja.kml"));
D5 = Pier(Kml.parse_pier("Bay\\Inkerman - 1.kml"));
D6 = Pier(Kml.parse_pier("Bay\\Inkerman - 2.kml"));

E1 = D1
E2 = D2
E3 = Pier(Kml.parse_pier("Bay\\Avlita.kml"));

=======
Caters = []
for c in caters:
	Caters.append(Ship(c))

A1 = Pier(Kml.parse_pier("Bay\\Grafskaja pristan.kml"));
A2 = Pier(Kml.parse_pier("Bay\\Severnaja kater.kml"));
B1 = Pier(Kml.parse_pier("Bay\\Art buhta parom.kml"));
B2 = Pier(Kml.parse_pier("Bay\\Severnaja parom.kml"));
C1 = Pier(Kml.parse_pier("Bay\\Art buhta kater.kml"));
C2 = Pier(Kml.parse_pier("Bay\\Radiogorka.kml"));
>>>>>>> 43a22185c5f478b4129b368fea5c994dad70685c

routes[0].piers = [A1, A2]
routes[1].piers = [B1, B2]
routes[2].piers = [C1, C2]
<<<<<<< HEAD
routes[3].piers = [D1, D2, D3, D4, D5, D6, D4, D3, D2]
routes[4].piers = [E1, E2, E3]
=======
>>>>>>> 43a22185c5f478b4129b368fea5c994dad70685c

#print grafskaya
#print nordside

data = scr.scrape_all_ships(caters)

def printpos():
	for cater in Caters:
		if (cater.ais_status() == "ONLINE") and (cater.route != -1) :
			route = routes[cater.route]
			if (cater.speed < MN.STOP):
<<<<<<< HEAD
				print Fore.RED , cater.nick, ": STAY AT :", route.destination(cater).name, ": ROUTE ON :", routes[cater.route].name
			else:
				print Fore.GREEN , cater.nick, ": ROUTE TO :", route.destination(cater).name, ":  ROUTE ON  :", routes[cater.route].name
#	for cater in Caters:
#		if (cater.ais_status() == "OFFLINE") :
#			print Fore.RED + Back.WHITE, "NOT FOUND : ", cater.nick
#
#	for cater in Caters:
#		if (cater.ais_status() == "ONLINE") and (cater.route == -1) :
#			print Fore.RED + Back.WHITE, "OUTSIDER : ", cater.nick
	print Fore.YELLOW, "------------------------------------------------------------------------------", Fore.RESET + Back.RESET + Style.RESET_ALL 
=======
				print cater.name, ": stay  at :", route.destination(cater).name
			else:
				print cater.name, ": route to :", route.destination(cater).name
>>>>>>> 43a22185c5f478b4129b368fea5c994dad70685c

def whatroute():
	for cater in Caters:
		if (cater.ais_status() == "ONLINE") :
			counter = []
			for route in routes:
				counter.append(route.verification(cater))
			maxpos = max(counter)
			if maxpos and (counter.count(maxpos) == 1):
				cater.route = counter.index(maxpos)
			elif maxpos:
				for i in range(len(counter)) :
					if cater.route == i:
						return
				cater.route = counter.index(maxpos)
<<<<<<< HEAD
			else:
				cater.route = -1

def upd(count):
	for i in range(count):
		time.sleep (90) #1.5 min delay
		data = scr.scrape_all_ships(caters)
		for cater in Caters :
			if cater.name in data:
				cater.update(data[cater.name])
			else:
				cater.update(None)

#timer = 35
#for t in range(timer):

#for c in Caters:
#	print c.nick#.encode("cp866")

#upd(1)
#whatroute()
#printpos()

while True:
	upd(3)
	whatroute()
	printpos()
#	print "----------------------------------"

#	print "----------------------------------"
#	#print "I am still work {0} minute remain".format(5 * (timer-t) )
#	#print "----------------------------------"
#	#time.sleep (2 * 60) #2 min delay
=======
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
>>>>>>> 43a22185c5f478b4129b368fea5c994dad70685c
