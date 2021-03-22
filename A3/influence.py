#!/usr/bin/env python3

import sys
import timeit
import math
import random
from queue import PriorityQueue
graph = sys.argv[1]
T = sys.argv[2]

# Creates an adjacency list from given graph input
# Input: string graph representing the name of the file
# Output: dict adjacencyList


def createGraph(graph):
    # Contains the elements in the graph represented in an adjacency list.
    adjacencyList = {}
    for line in open(graph, "r"):
        elements = line.split()

        if(elements[0] not in adjacencyList):
            adjacencyList[elements[0]] = [[elements[1], elements[2]]]
        else:
            adjacencyList[elements[0]].append([elements[1], elements[2]])

    return adjacencyList

# Finds all unique members from the given graph input
# Input: string graph representing the name of the file
# Output: list uniqueMembers


def findMembers(graph):
    uniqueMembers = []
    for line in open(graph, "r"):
        elements = line.split()
        if(elements[0] not in uniqueMembers):
            uniqueMembers.append(elements[0])
        if(elements[1] not in uniqueMembers):
            uniqueMembers.append(elements[1])

    return uniqueMembers

# Finds the shortest path from a given startNode to all other uniqueMembers
# Input: dict adjacencyList, string startNode, list uniqueMembers
# Output: dict distanceSet, which represents the distance from the startNode to all other nodes


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

            # Node already exists at a lower cost
            if pathDistance > distanceSet[adjacentNode]:
                continue

            if(pathDistance < distanceSet[str(adjacentNode)]):
                distanceSet[adjacentNode] = pathDistance
                queue.put((pathDistance, int(adjacentNode)))

    return distanceSet

# Gathers the spread of each member by calling findShortestPath for each member
# Input: dict adjacencyList, list uniqueMembers, string T
# Output: dict memberSpread, whih represents the spread of each member in a dictionary format


def spreadForEachMember(adjacencyList, uniqueMembers, T):
    memberSpread = {}
    for member in uniqueMembers:
        distanceSet = findShortestPaths(adjacencyList, member, uniqueMembers)
        spread = len(
            [node for node in distanceSet.values() if float(node) <= float(T)])
        memberSpread[member] = spread

    return memberSpread

# Finds the max spread given memberSpread
# Input: list memberSpread
# Output: (maxKey, maxValue), which represents the member with the max spread as well as the value of the spread


def findMaxSpread(memberSpread):
    valueList = list(memberSpread.values())
    keyList = list(memberSpread.keys())

    maxKey = keyList[valueList.index(max(valueList))]
    maxValue = max(valueList)
    return (maxKey, maxValue)


def CreateExpGraphs(edges):
    nodes = 100
    density = edges/nodes
    rows = 100 * math.ceil(density)

    vertex = 0
    with open('graph_{}.txt'.format(density), 'w') as file:
        for i in range(rows):
            count_vertex = 0
            while count_vertex < math.ceil(density) and vertex <= nodes:
                file.write(str(vertex) + ' ' + str(random.randint(0, nodes)
                                                   ) + ' ' + str(random.uniform(0.0, 4.99)) + '\n')
                count_vertex += 1
            vertex += 1


def graphTop1Influencer():
    list_files = ['graph_2.0.txt',
                  'graph_3.0.txt',
                  'graph_4.0.txt',
                  'graph_5.0.txt',
                  'graph_6.0.txt',
                  'graph_7.0.txt',
                  'graph_8.0.txt',
                  'graph_9.0.txt',
                  'graph_10.0.txt',
                  'graph_11.0.txt']

    time_record = []
    for graph in list_files:
        start_time = timeit.default_timer()
        adjacencyList = createGraph(graph)
        uniqueMembers = findMembers(graph)
        memberSpread = spreadForEachMember(adjacencyList, uniqueMembers, T)
        (maxKey, maxValue) = findMaxSpread(memberSpread)
        stop_time = timeit.default_timer()

        time_record.append(str(round((stop_time-start_time), 2)))

    return time_record


def plot(time_record):
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('Agg')
    x = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    y = time_record

    plt.xlabel('Density (Edges/Nodes)')
    plt.ylabel('Time to Find Top 1 Influencer (s)')
    plt.title('Time vs Graph Density to find Top 1 Influencer')
    plt.xticks(x)
    plt.plot(x, y, '.-')
    plt.show()
    plt.savefig('Density_Graph_Top1.png')


if __name__ == '__main__':

    start_time = timeit.default_timer()
    adjacencyList = createGraph(graph)
    uniqueMembers = findMembers(graph)
    memberSpread = spreadForEachMember(adjacencyList, uniqueMembers, T)
    (maxKey, maxValue) = findMaxSpread(memberSpread)
    stop_time = timeit.default_timer()

    print("TOP-1 INFLUENCER: " + str(maxKey) + ", SPREAD: " +
          str(maxValue) + ", TIME: " + str(round((stop_time-start_time), 2)))
