#1st
#2nd
#3
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
