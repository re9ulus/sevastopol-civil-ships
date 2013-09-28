from scrapper import Scrapper
from ship import Ship
from area import Area
from coordinates import Coordinates
from kmlparser import KmlParser


Kml = KmlParser()

City_Nord_bay = Kml.parse("Bay\\City-Nord.kml")
City_Nord_bay.start_point()

Art_Nord_bay = Kml.parse("Bay\\Art-Nord.kml")
Art_Nord_bay.start_point()

caters = ["OST", "ORION", "G. OVCHINNIKOV", "ZUYD", "PERSEY", "MOLODIZGNIY", "ADMIRAL LAZAREV", "SATURN", "ADMIRAL ISTOMIN", "V ADMIRAL KLOKACHEV", "NORD"]
Caters = []
for c in caters:
	Caters.append(Ship(c))


Scrap = Scrapper()


City_Nord = []
Art_Nord = []
Not_Found = []
Outsiders = []

for cater in Caters :
	res = Scrap.scrape_ship(cater.name)
	if res == None:
		Not_Found.append(cater.name)
	else:
		f1 = f2 = False
		v, cors, point = res
		if City_Nord_bay.inside(point) == "INSIDE":
			City_Nord.append(cater.name)
			f1 = True
		if Art_Nord_bay.inside(point) == "INSIDE":
			Art_Nord.append(cater.name)
			f2 = True

		if not (f1 or f2):
			Outsiders.append(cater.name)

		#print point
		#print

print "City - Nord - bay"
for cater in City_Nord:
	print cater

print

print "Art - Nord - bay"
for cater in Art_Nord:
	print cater

print

print "Outsider"
for cater in Outsiders:
	print cater

print

print "Not Found"
for cater in Not_Found:
	print cater