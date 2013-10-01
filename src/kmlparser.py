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
        return: str_name, [Coordinates(latitude, longitude)]
        '''
        try:
            placemark = parse(path).getElementsByTagName("Placemark")[0]        
            coordinates = placemark.getElementsByTagName("coordinates")[0].childNodes[0].nodeValue
            #Warning ENCODE CP 866 
            name = placemark.getElementsByTagName("name")[0].childNodes[0].nodeValue.encode("CP866")

            polygon = []
            for coord in coordinates.split():
                #print "#", coord, "#"
                longitude, latitude, altitude = [float(c) for c in coord.split(",") if c != ""]
                polygon.append(Coordinates(latitude, longitude))
                #print Coordinates(latitude, longitude)
            res = name, Area(polygon)
        except:
            res = None
        finally:
            return res

    def parse_pier(self, path):
        '''
        Parse coordinate from klm file.
        return: (str_name, [Coordinates(latitude, longitude)], Coordinates(latitude, longitude) )
        '''
        try:
            LookAt = parse(path).getElementsByTagName("LookAt")[0]
            latitude = float(LookAt.getElementsByTagName("latitude")[0].childNodes[0].nodeValue)
            longitude = float(LookAt.getElementsByTagName("longitude")[0].childNodes[0].nodeValue)
            mark = Coordinates(latitude, longitude)
            #print mark

            area = self.parse(path)
            res = area[0], area[1], mark
        except:
            res = None
        finally:
            #print res
            return res
