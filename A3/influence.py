#!/usr/bin/env python3

import sys
import timeit
import math
from queue import PriorityQueue
graph = "facebook_small.txt" #sys.argv[1] 
T = 5 #sys.argv[2]

#Creates an adjacency list from given graph input
#Input: string graph representing the name of the file
#Output: dict adjacencyList
def createGraph(graph): 
    adjacencyList = {} #Contains the elements in the graph represented in an adjacency list.
    for line in open(graph, "r"):
        elements = line.split()
        
        if(elements[0] not in adjacencyList):
            adjacencyList[elements[0]] = [[elements[1], elements[2]]]
        else:
            adjacencyList[elements[0]].append([elements[1], elements[2]])
    
    return adjacencyList

#Finds all unique members from the given graph input
#Input: string graph representing the name of the file
#Output: list uniqueMembers
def findMembers(graph):
    uniqueMembers = []
    for line in open(graph, "r"):
        elements = line.split()
        
        if(elements[0] not in uniqueMembers):
            uniqueMembers.append(elements[0])
        if(elements[1] not in uniqueMembers):
            uniqueMembers.append(elements[1])
    
    return uniqueMembers

#Finds the shortest path from a given startNode to all other uniqueMembers
#Input: dict adjacencyList, string startNode, list uniqueMembers
#Output: dict distanceSet, which represents the distance from the startNode to all other nodes
def findShortestPaths(adjacencyList, startNode, uniqueMembers):
    distanceSet = {node: math.inf for node in uniqueMembers}
    distanceSet[startNode] = 0
    queue = PriorityQueue()
    queue.put((0, int(startNode)))
    while not queue.empty():
        (distance, node) = queue.get()
        if str(node) not in adjacencyList:
            continue
        for adjacentNode, weightDistances in adjacencyList[str(node)]:
            pathDistance = distance + float(weightDistances)
            
            if pathDistance > distanceSet[adjacentNode]: #Node already exists at a lower cost
                continue
            
            if(pathDistance < distanceSet[str(adjacentNode)]):
                distanceSet[adjacentNode] = pathDistance
                queue.put((pathDistance, int(adjacentNode)))

    return distanceSet

#Gathers the spread of each member by calling findShortestPath for each member
#Input: dict adjacencyList, list uniqueMembers, string T
#Output: dict memberSpread, whih represents the spread of each member in a dictionary format
def spreadForEachMember(adjacencyList, uniqueMembers, T):
    memberSpread = {}
    for member in uniqueMembers:
        distanceSet = findShortestPaths(adjacencyList, member, uniqueMembers)
        spread =  len([node for node in distanceSet.values() if float(node) <= T])
        memberSpread[member] = spread
    
    return memberSpread

#Finds the max spread given memberSpread
#Input: list memberSpread
#Output: (maxKey, maxValue), which represents the member with the max spread as well as the value of the spread
def findMaxSpread(memberSpread):
    valueList = list(memberSpread.values())
    keyList = list(memberSpread.keys())
    
    maxKey = keyList[valueList.index(max(valueList))]
    maxValue = max(valueList)
    return (maxKey, maxValue)
    
start_time = timeit.default_timer()
adjacencyList = createGraph(graph)
uniqueMembers = findMembers(graph)
memberSpread = spreadForEachMember(adjacencyList, uniqueMembers, T)
(maxKey, maxValue) = findMaxSpread(memberSpread)
stop_time = timeit.default_timer()
print("TOP-1 INFLUENCER: " + str(maxKey) + ", SPREAD: " + str(maxValue) + ", TIME: " + str(round((stop_time-start_time),2)))

        
        
