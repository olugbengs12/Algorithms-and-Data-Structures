#Dijkstra Shortest path
import sys
import heapq


class vertex(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacencieslist = []
        self.mindistance = sys.maxsize

    def __cmp__(self, othervertex):  #overridding the comparator operation
        return self.cmp(self.mindistance, othervertex.mindistance)

    def __lt__(self, othervertex):  #overriding the less than operation
         selfpriority = self.mindistance
         othervertexpriority = othervertex.mindistance
         return selfpriority < othervertexpriority

class edge:
    def __init__(self, weight, startvertex, targetvertex):
        self.weight = weight
        self.startvertex = startvertex
        self.targetvertex = targetvertex

class Algorithm(vertex, edge):
    def calculateshortestpath(self, startvertex):
        queue = []
        startvertex.mindistance = 0
        heapq.heappush(queue, startvertex)

        while len(queue) > 0:               #since priority queue, pop will return the element with smallest length
            actual_vertex = heapq.heappop(queue)
            for edge in actual_vertex.adjacencieslist:
                initial = edge.startvertex
                final = edge.targetvertex
                newdistance = initial.mindistance + edge.weight

                if newdistance < final.mindistance:
                    final.predecessor = initial
                    final.mindistance = newdistance
                    heapq.heappush(queue, final)

    def getshortestpath(self, targetvertex):
        print('Shortest path to target is: ' + targetvertex.mindistance)

        node = targetvertex     #backtracking to get the nodes that were visited to obtain this minimum value of distance
        while node is not None:
            print(node.name)
            node = node.predecessor


node1 = vertex('A')
node2 = vertex('B')
node3 = vertex('C')

edge1 = edge(1, node1, node2)
edge2 = edge(1, node2, node3)
edge3 = edge(0.1, node1, node3)

node1.adjacencieslist.append(node1)
node1.adjacencieslist.append(node2)
node2.adjacencieslist.append(node3)

vertexlist = [node1, node2, node3]

algorithm = Algorithm(node1)
algorithm.calculateshortestpath(node1)
algorithm.getshortestpath(node3)

#This is a test
