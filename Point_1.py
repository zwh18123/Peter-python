#1st
#n1-1
#n1-2
#m-github
#n2
#bran-n3
# local n2
#ln2-1

import math
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return(str(self.x) + "  " + str(self.y))


    def distance(self, otherpoint):
        a = self.x - otherpoint.x
        b = self.y - otherpoint.y
        return math.sqrt(a ** 2 + b ** 2)
        #        return ("{:.2f}".format(math.sqrt(a**2 + b**2)))
