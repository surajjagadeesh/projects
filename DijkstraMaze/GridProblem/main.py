#Gets all of the inputs for the grid problem--the size of the grid, the source
#location, the destination location, and the location of all obstacles--and then
#uses the dijkstra algorithm to see whether the problem is solvable or not. If it
#is solvable, prints the fastest valid path from the source to the destination
#@author: Suraj Jagadeesh
#@version: 6/22/2017

import re
import point
from inputs import *
from dijkstra import *

inputs = getInputs()

evaluateDijkstra(inputs)
