import re
import point
import inputs
import dijkstra

size = raw_input('Enter the size of the square grid: ')
while(not size.isdigit() or int(size) < 1):
    print 'Invalid Input...'
    size = raw_input('Enter the size of the square grid: ')
size = int(size)

def validPosition(type):
    validPos = re.compile('^[0-9]+,[0-9]+$') #regex
    pos = raw_input("What is the " + type + " (use row,column format): ")
    if(validPos.match(pos)):
        location = point.Point(pos)
    while(not validPos.match(pos) or not location.validPoint(size)): #while it's not a valid regex or the point isnt valid
        print 'Invalid Input...'
        pos = raw_input("What is the " + type + " (use row,column format): ")
        while(not validPos.match(pos)):
            print 'Invalid Input...'
            pos = raw_input("What is the " + type + " (use row,column format): ")
        location = point.Point(pos)
    return location

source = validPosition('source')
destination = validPosition('destination')

def invalidBlockEntries(blocks):
    blockArray = blocks.split()
    for block in blockArray:
        location = point.Point(block)
        if(not location.validPoint(size) or location == source or location == destination): #if it's not valid, returns true
            return True
    return False

validBlocks = re.compile('^[0-9]+,[0-9]+( [0-9]+,[0-9]+)*$')
blocks = raw_input("What are the position of the block(s) (use row,column row,column etc. format): ")
while(not validBlocks.match(blocks) or invalidBlockEntries(blocks)):
    print 'Invalid Input...'
    blocks = raw_input("What are the position of the block(s) (use row,column row,column etc. format): ")

blocks = blocks.split()
for x in range(0,len(blocks)):
    blocks[x] = point.Point(blocks[x])

distance = {}
unvisited = []
for x in range(0,size):
    for y in range(0,size):
        try:
            location = point.Point(str(x) + ',' + str(y))
            index = blocks.index(location)
        except ValueError:
            unvisited.append(location.to_string())
            distance[location.to_string()] = [size**2, []]

distance[source.to_string()][0] = 0
distance[source.to_string()][1] = [source.to_string()]


#distance["1,2"][1][0] first position of list
#distance["1,2"][0] distance
def dijkstraAlgorithm():
    smallest = size**2
    source = ""
    for key in unvisited:
        if(distance[key][0] < smallest):
            smallest = distance[key][0]
            source = key

    if(smallest == size**2): #if everything is unreachable
        return str(-1)

    if(source == destination.to_string()):
        return distance[source][1]

    source = point.Point(source)

    neighbors = [point.Point(str(source.x+1) + ',' + str(source.y)), point.Point(str(source.x-1) + ',' + str(source.y)),
                point.Point(str(source.x) + ',' + str(source.y+1)), point.Point(str(source.x) + ',' + str(source.y-1))]

    for x in range (0,4):
        if(neighbors[x].validPoint(size) and neighbors[x] not in blocks):
            if(distance[source.to_string()][0] + 1 < distance[neighbors[x].to_string()][0]):
                distance[neighbors[x].to_string()][0] = distance[source.to_string()][0] + 1 #changing distance
                distance[neighbors[x].to_string()][1] = list(distance[source.to_string()][1])
                distance[neighbors[x].to_string()][1].append(neighbors[x].to_string())
    unvisited.remove(source.to_string())
    return dijkstraAlgorithm()

response = dijkstraAlgorithm()
if(response == '-1'):
    print 'There is no path from your source to your destination'
else:
    print 'There is a path from your source to your destination!'
    print 'The path is:'
    print response
