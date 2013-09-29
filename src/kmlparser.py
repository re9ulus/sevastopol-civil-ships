from xml.dom.minidom import *
from coordinates import Coordinates
from area import Area

class KmlParser:
    '''
    KmlParser class.
    '''
    def __init__(self):
        pass

    def parse(self, path):
        '''
        Parse coordinate from klm file.
        return: [Coordinates(latitude, longitude)]
        '''
        try:
            kml = parse(path)
            coordinates = kml.getElementsByTagName("coordinates")[0].childNodes[0].nodeValue
            #print coordinates
            polygon = []
            for coord in coordinates.split():
                #print "#", coord, "#"
                longitude, latitude, altitude = [float(c) for c in coord.split(",") if c != ""]
                polygon.append(Coordinates(latitude, longitude))
                #print Coordinates(latitude, longitude)
            res = Area(polygon)
        except:
            res = None
        finally:
            return res