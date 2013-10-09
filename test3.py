from scrapper import Scrapper
from ship import Ship
from area import Area
from coordinates import Coordinates
from kmlparser import KmlParser


Kml = KmlParser()

#print "start parse bay"
City_Nord_bay = Kml.parse("Bay\\City-Nord.kml")
Art_Nord_bay = Kml.parse("Bay\\Art-Nord.kml")
Art_Rad_bay = Kml.parse("Bay\\Art-Rad.kml")
#print "end parse bay"

caters = ["OST", "ORION", "G. OVCHINNIKOV", "ZUYD", "PERSEY", "MOLODIZGNIY", "ADMIRAL LAZAREV", "SATURN", "ADMIRAL ISTOMIN", "V ADMIRAL KLOKACHEV", "NORD"]
Caters = []
for c in caters:
	Caters.append(Ship(c))


#Scrap = Scrapper()

City_Nord = []
Art_Nord = []
Art_Rad = []
Not_Found = []
Outsiders = []

for cater in Caters :
	#res = Scrap.scrape_ship(cater.name)
	cater.update_from_ais()
	point = cater.coordinates
	if point == None:
		Not_Found.append(cater.name)
	else:
		f1 = f2 = f3 = False
		#v, cors, point = res
		if City_Nord_bay.inside(point) == "INSIDE":
			City_Nord.append(cater.name)
			f1 = True
		if Art_Nord_bay.inside(point) == "INSIDE":
			Art_Nord.append(cater.name)
			f2 = True
		if Art_Rad_bay.inside(point) == "INSIDE":
			Art_Rad.append(cater.name)
			f3 = True

		if not (f1 or f2 or f3):
			Outsiders.append(cater.name)

		#print point
		#print

print "-= City - Nord - bay =-"
for cater in City_Nord:
	print cater

print

print "-= Art - Nord - bay =-"
for cater in Art_Nord:
	print cater

print

print "-= Art - Rad - bay =-"
for cater in Art_Rad:
	print cater

print

print "-= Outsider =-"
for cater in Outsiders:
	print cater

print

print "-= Not Found =-"
for cater in Not_Found:
	print cater