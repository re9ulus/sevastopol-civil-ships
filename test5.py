from src.coordinates import Coordinates
#from math import *
from src.ship import Ship
from src.area import Area
from src.kmlparser import KmlParser
from src.route import Route
from src.pier import Pier
from src.scrapper import Scrapper 
from src.magic_numbers import MN

from colorama import init
from colorama import Fore, Back, Style
init()

import time
from time import gmtime, strftime

Kml = KmlParser()

routes = [
Route(Kml.parse("Bay\\Gorod - Severnaja.kml")),
Route(Kml.parse("Bay\\Artbuhta - Severnaja.kml")),
Route(Kml.parse("Bay\\Artbuhta - Radiogorka.kml")),
Route(Kml.parse("Bay\\Gorod - Gollandija - Inkerman.kml")),
Route(Kml.parse("Bay\\Gorod - Avlita.kml"))
]

caters = []
Caters = []

for name in open("ship.list", "r").readlines():
	Caters.append(Ship(name.split("/")))
	caters.append(name.split("/")[0])

#print caters

scr = Scrapper()
#scr = scr.scrape_all_ships(scr)

A1 = Pier(Kml.parse_pier("Bay\\Grafskaja pristan.kml"));
A2 = Pier(Kml.parse_pier("Bay\\Severnaja kater.kml"));

B1 = Pier(Kml.parse_pier("Bay\\Art buhta parom.kml"));
B2 = Pier(Kml.parse_pier("Bay\\Severnaja parom.kml"));

C1 = Pier(Kml.parse_pier("Bay\\Art buhta kater.kml"));
C2 = Pier(Kml.parse_pier("Bay\\Radiogorka.kml"));

D1 = Pier(Kml.parse_pier("Bay\\Pirs u porta.kml"));
D2 = Pier(Kml.parse_pier("Bay\\Apolonovka.kml"));
D3 = Pier(Kml.parse_pier("Bay\\Gollandija.kml"));
D4 = Pier(Kml.parse_pier("Bay\\Ugolnaja.kml"));
D5 = Pier(Kml.parse_pier("Bay\\Inkerman - 1.kml"));
D6 = Pier(Kml.parse_pier("Bay\\Inkerman - 2.kml"));

E1 = D1
E2 = D2
E3 = Pier(Kml.parse_pier("Bay\\Avlita.kml"));

DeadEnd = Pier(Kml.parse_pier("Bay\\Dead end.kml"));

routes[0].piers = [A1, A2]
routes[1].piers = [B1, B2]
routes[2].piers = [C1, C2]
routes[3].piers = [D1, D2, D3, D4, D5, D6, D4, D3, D2]
routes[4].piers = [E1, E2, E3, E2]

data = scr.scrape_all_ships(caters)

def printpos():
	print time.strftime("%a, %d %b %Y, %H:%M", gmtime())
	for cater in Caters:
		try:
			if (cater.deadend(DeadEnd)):
				print Fore.RED, Style.DIM, cater

			elif (cater.ais_status() == "ONLINE") :
				if (cater.route != None) :
					route = routes[cater.route]
					if (cater.speed < MN.STOP):
						print Fore.CYAN, Style.BRIGHT, cater.nick, ": STAY AT :", route.destination(cater).name, ": ROUTE ON :", routes[cater.route].name
					else:
						print Fore.GREEN, Style.BRIGHT, cater.nick, ": ROUTE TO :", route.destination(cater).name, ":  ROUTE ON  :", routes[cater.route].name
				else:
					print Fore.YELLOW, Style.DIM, cater
			elif (cater.ais_status() == "OFFLINE") :
				print Fore.BLACK, Style.BRIGHT, cater
								
		except:
			print Fore.RED + Back.YELLOW, cater, route, Fore.RESET + Back.RESET + Style.RESET_ALL 

	print Fore.YELLOW, Style.BRIGHT, "------------------------------------------------------------------------------", Fore.RESET + Back.RESET + Style.RESET_ALL 


def whatroute():
	for cater in Caters:
		if (cater.ais_status() == "ONLINE") :
			
			if (cater.deadend(DeadEnd)):
				continue

			counter = []
			for route in routes:
				counter.append(route.verification(cater))
			maxpos = max(counter)
			
			if (not maxpos):
				cater.route = None
				continue

			if (cater.route != None) and (routes[cater.route] == maxpos):
				continue
			
			cater.route = counter.index(maxpos)

def upd(count):
	for i in range(count):
		time.sleep (90) #1.5 min delay
		data = scr.scrape_all_ships(caters)
		for cater in Caters :
			if cater.name in data:
				cater.update(data[cater.name])
			else:
				cater.update(None)

while True:
	printpos()
	upd(3)
	whatroute()
