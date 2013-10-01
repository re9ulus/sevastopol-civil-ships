from area import Area

class Pier:
    '''
    A Pier class
    '''
    def __init__(self, name, pier, mark) :
        self.name = name
        self.area = pier
        self.mark = mark

    def __init__(self, parser) :
    	'''
    	Parser (str, Area, Coordinates)
    	'''
    	#print parser
        self.name = parser[0]
        self.area = parser[1]
        self.mark = parser[2]

    def __str__(self):
    	#print self.name
        return "pier: {0}; orientir mark: {1}".format(self.name, self.mark)