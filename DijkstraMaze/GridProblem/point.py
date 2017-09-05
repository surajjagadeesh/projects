#Basic point class with a comparable, toString, and a function to check if
#it is a valid point given a size of a square grid.
#@author: Suraj Jagadeesh
#@version: 6/22/2017
class Point:

    #Constructor, takes x and y values
    #@param value: A list with two indices, the first being the x value, the
    #second being the y value
    def __init__(self, value):
        values = value.split(',')
        self.x = int(values[0])
        self.y = int(values[1])

    #Basic Comparable function, first compares on x then on y
    def __cmp__(self, other):
        if self.x > other.x: return 1
        if self.x < other.x: return -1
        if self.y > other.y: return 1
        if self.y < other.y: return -1
        #it's a tie
        return 0

    #Prints the string in a x,y format
    def to_string(self):
        return str(self.x) + ',' + str(self.y)

    #Checks if the point is valid in the specified grid
    #@param size: The size of the grid you want to check if the point is valid
    def validPoint(self, size):
        return (self.x < size and self.x > -1 and self.y < size and self.y > -1)
