"""
Graph implementation on educative.com
"""

from collections import deque


class AdjNode:
    """
    A class to represent the adjacency list of the node
    """

    def __init__(self, data):
        """
        Constructor
        :param data : vertex
        """
        self.vertex = data
        self.next = None


class Graph:
    """
    Graph Class ADT
    """

    def __init__(self, vertices):
        """s
        Constructor
        :param vertices : Total vertices in a graph
        """
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, source, destination):
        """
        add edge
        :param source: Source Vertex
        :param destination: Destination Vertex
        """

        # Adding the node to the source node
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        # Adding the source node to the destination if undirected graph

        # Intentionally commented the lines
        #node = AdjNode(source)
        #node.next = self.graph[destination]
        #self.graph[destination] = node

    def print_graph(self):
        """
        A function to print a graph
        """
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


    def bfs(self, source=0):
        """
        Breadth-First Search
        :param source: Starting Vertex
        :return: List of vertices in BFS order
        """
        visited = [False] * self.V
        result = []
        queue = deque()

        # Enqueue the source vertex
        queue.append(source)
        visited[source] = True

        while queue:
            current = queue.popleft()
            result.append(current)

            # Explore all adjacent vertices
            temp = self.graph[current]
            while temp:
                if not visited[temp.vertex]:
                    queue.append(temp.vertex)
                    visited[temp.vertex] = True
                temp = temp.next

        return result