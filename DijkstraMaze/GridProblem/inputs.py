#The inputs file gets all the necessary inputs for the grid problem. More
#specifically, it gets the grid size, the source, the destination, and the
#location of all the blocks/obstacles.
#@author: Suraj Jagadeesh
#@version: 6/22/2017

import re
import point

#Asks the user for the size of the square grid, will keep asking until the
#user provides a valid, positive non-zero integer
#@return: Returns the valid whole number
def getSize():
    size = raw_input('Enter the size of the square grid: ')
    while(not size.isdigit() or int(size) < 2): #while it's not a valid number
        print 'Invalid Input...'
        size = raw_input('Enter the size of the square grid: ')
    size = int(size) #raw_input stores as a string so must convert to int once it is valid
    return size

size = getSize() #sets size as a global variable since almost all functions utilize this

#Prompts the user for a valid point in the format row,column (with no spaces)
#@param type: Either 'source' or 'destination' in order to ask the respective question
#@return: Returns a point representing a valid location
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

#Checks if the given list of blocks is valid, meaning it is in the grid and it is
#not on the same point as the source or destination
#@param source: The source point
#@param destination: The destination point
#@param blocks: List of blocks that is going to be checked
#@return: Returns true if any block in the list of blocks is invalid, false otherwise
def invalidBlockEntries(source, destination, blocks):
    blockArray = blocks.split() #splits by spaces such that each location is in its own index
    for block in blockArray:
        location = point.Point(block)
        if(not location.validPoint(size) or location == source or location == destination): #if it's not valid, returns true
            return True
    return False

#Promps the user to input the location of all of the obstacles in the
#row,column row,column row,column etc. format. These blocks must be in the
#grid and can't be on the source or destination
#@param source: The source point
#@param destination: The destination Point
#@return: Returns a valid list of points represnting all obstacles
def getBlocks(source, destination):
    validBlocks = re.compile('^[0-9]+,[0-9]+( [0-9]+,[0-9]+)*$') #regex
    blocks = raw_input("What are the position of the block(s) (use row,column row,column etc. format): ")
    while(not validBlocks.match(blocks) or invalidBlockEntries(source, destination, blocks)):
        print 'Invalid Input...'
        blocks = raw_input("What are the position of the block(s) (use row,column row,column etc. format): ")
    blocks = blocks.split()
    for x in range(len(blocks)):
        blocks[x] = point.Point(blocks[x])
    return blocks

#Asks the user to input all of the necessary information, including the
#source position, destination position, and the location of all blocks.
#@return: A list with 4 indices, the first being the size of the square grid,
#the second being the point representing the source, the third being the point
#representing the destination, and the last being a list of points representing
#the location of all obstacle/blocks.
def getInputs():
    source = validPosition('source')
    destination = validPosition('destination')
    blocks = getBlocks(source, destination)
    return [size, source, destination, blocks]
