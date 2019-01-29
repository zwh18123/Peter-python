from Polygon import Polygon
from Point_1 import Point


class Rectangle(object):
    def __init__(self,Point):
        super(Rectangle, self).__init__()
        self.length = Point.x
        self.width = Point.y



    def perimeter(self):
        print("Using Rectangle's perimeter routine")
        return 2 * self.length + 2 * self.width


