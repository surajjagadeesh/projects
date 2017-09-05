#The Dijkstra File uses the dijkstra algorithm, trying to find the fastest path
#from the source to the destination, taking into account all of the
#obstacles in the way. There are 6 steps in the dijkstra algorithm,
#1. Assign every location an infinitely high distance value (size^2 in our case) and
#set the distance of the source to 0.
#2. Start from the initial node, mark every other node as unvisited
#3. Look at all neighbors of the current node, and look at their tentative distance.
#For example, if the distance of the current node being visited is 6, and the next
#neighbor is 1 distance away, the tentative distance would then become 7. If this
#tentative distance is less than the distance value it currently has, update the
#distance and path, otherwise do nothing.
#4. After looking at all the neighbors of the current node, make the current
#node visited, and remove it from the unvisited list. Visited nodes will not
#be visited again.
#5. Run the algorithm starting at step 3 with the node in unvisited that has the
#lowest distance. Repeat recursively
#6. This process will eventually end either when the stored distance of all the
#unvisited locations are size^2, indicating that all of these locations was never
#a valid neighbor node, meaning that all of these locations are not accessible,
#or when the destination locations has been visited. This either prints that there
#is no valid path or prints the fastest path from the source to the destination.
#@author: Suraj Jagadeesh
#@date: 6/22/2017

import point

#Creates a dictionary and a list of all non-obstacle spaces
#@param size: The size of the grid
#@param blocks: The list of the location of the blocks
#@param source: The position of the source
#@return: Returns a list, with the first index being a dictionary
#that uses locations as a key, and has a 2 index list as its value
#with the first index being the total distance from the source to the
#location (default set at size squared - the max possible), and the second
#being an empty array that is going to store multiple positions, representing
#the path to get to the location
def prepareDijkstra(size, blocks, source):
    distance = {}
    unvisited = []
    for x in range(size): #looks at every possible point in the grid
        for y in range(size):
            location = point.Point(str(x) + ',' + str(y))
            if(location not in blocks): #adds to the unvisited/distance if there is not an obstacle
                unvisited.append(location.to_string())
                distance[location.to_string()] = [size**2, []]

    distance[source.to_string()][0] = 0 #Need to start the dijkstra algorithm from the source
    distance[source.to_string()][1] = [source.to_string()] #Give the source's path its own location
    return [distance, unvisited]



#Runs the recursive dijkstraAlgorithm on the unvisited point that has the least
#distance value. Upon fully running, every valid position will either have
#the distance it takes to get there and the valid path, or will have a distance
#of size^2, indicating that the location is not accessible.
#@param size: Size of the square grid
#@param destination: The point of destination
#@param unvisitedPaths: A list containing two items, the first being the
#distance dictionary and the second being an array with all unvisited locations
#@param blocks: A list of all points that have blocks/obstacles on them
#@return: Returns the path to the destination if possible, otherwise returns
# '-1' if the destination is not accessible
def dijkstraAlgorithm(size, destination, unvisitedPaths, blocks):
    distance = unvisitedPaths[0] #dictionary storing distance/paths
    unvisited = unvisitedPaths[1] #array storing unvisited locations

    smallest = size**2 #default value of distances
    source = ""
    for key in unvisited:
        if(distance[key][0] < smallest): #looks for the nearest accessible location
            smallest = distance[key][0]
            source = key

    if(smallest == size**2): #if everything is unreachable
        return str(-1)

    if(source == destination.to_string()): #if source has been visited
        return distance[source][1]

    source = point.Point(source) #converts the starting location to a point

    neighbors = [point.Point(str(source.x+1) + ',' + str(source.y)), point.Point(str(source.x-1) + ',' + str(source.y)),
                point.Point(str(source.x) + ',' + str(source.y+1)), point.Point(str(source.x) + ',' + str(source.y-1))]

    for x in range(4):
        if(neighbors[x].validPoint(size) and neighbors[x] not in blocks): #if it's a valid accessible location
            if(distance[source.to_string()][0] + 1 < distance[neighbors[x].to_string()][0]):
                distance[neighbors[x].to_string()][0] = distance[source.to_string()][0] + 1 #changing distance
                distance[neighbors[x].to_string()][1] = list(distance[source.to_string()][1])
                distance[neighbors[x].to_string()][1].append(neighbors[x].to_string()) #changes the path

    unvisited.remove(source.to_string()) #removes the source location from the unvisited locations
    return dijkstraAlgorithm(size, destination, unvisitedPaths, blocks)

#Takes the inputs, prepares, and runs the dijkstra algorithm.
#@param inputs: A list with 4 indices, the first being the size of the square grid,
#the second being the point representing the source, the third being the point
#representing the destination, and the last being a list of points representing
#the location of all obstacle/blocks.
#If given all the information the destination is not accessible, prints that
#there is no valid path, otherwise, prints that there is a valid path followed
#by the valid path itself
def evaluateDijkstra(inputs):
    size = inputs[0]
    source = inputs[1]
    destination = inputs[2]
    blocks = inputs[3]
    unvisited = prepareDijkstra(size, blocks, source)
    response = dijkstraAlgorithm(size, destination, unvisited, blocks)
    if(response == '-1'):
        print 'There is no path from your source to your destination'
    else:
        print 'There is a path from your source to your destination!'
        print 'The path is: %s' %response
