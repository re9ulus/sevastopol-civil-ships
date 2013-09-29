from area import Area

class Route:
    '''
    A Route class
    '''
    def __init__(self, name, bay=None, piers=None) :
        self.name = name
        self.bay = bay
        self.piers = piers

    def __str__(self):
        return "route: {0};".format(self.name)