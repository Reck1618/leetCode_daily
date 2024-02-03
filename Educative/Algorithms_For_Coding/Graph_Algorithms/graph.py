"""
Graph implementation on educative.com - Directed Graph
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

    def resize_graph(self, new_size):
        """
        Resize the graph array
        :param new_size: New size of the graph array
        """
        new_graph = [None] * new_size
        for i in range(self.V):
            new_graph[i] = self.graph[i]
        self.graph = new_graph
        self.V = new_size

    def add_node(self, data):
        """
        Add node
        :param data: Vertex to be added
        """
        if data < 0:
            print("Vertex index should be non-negative.")
            return

        if data >= self.V:
            self.resize_graph(data + 1)

        if self.graph[data] is not None:
            print(f"Node {data} already exists")
            return

        node = AdjNode(data)
        self.graph[data] = node

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

    def remove_edge(self, source, destination):
        """
        Remove edge
        :param source: Source Vertex
        :param destination: Destination Vertex
        """
        # Remove the node from the source node
        temp = self.graph[source]
        if temp and temp.vertex == destination:
            self.graph[source] = temp.next
            return

        while temp:
            if temp.vertex == destination:
                break
            prev = temp
            temp = temp.next

        if not temp:
            return

        prev.next = temp.next

    def remove_vertex(self, vertex):
        """
        Remove vertex
        :param vertex: Vertex to be removed
        """
        # Iterating over all vertices to remove the specified vertex from their adjacency lists
        for i in range(self.V):
            if i != vertex:
                temp = self.graph[i]
                while temp:
                    if temp.vertex == vertex:
                        self.remove_edge(i, vertex)
                        break
                    temp = temp.next

        self.graph[vertex] = None

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

    def dfs(self, source=0):
        """
        Depth-First Search
        :param source: Starting Vertex
        :return: List of vertices in DFS order
        """
        visited = [False] * self.V
        result = []
        stack = []

        stack.append(source)

        while stack:
            current = stack.pop()

            if not visited[current]:
                result.append(current)
                visited[current] = True

            current_neighbor = self.graph[current]
            while current_neighbor:
                if not visited[current_neighbor.vertex]:
                    stack.append(current_neighbor.vertex)
                current_neighbor = current_neighbor.next

        return result


# Main to test the above program
if __name__ == "__main__":
    V = 5
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_node(5)
    g.add_edge(2, 5)

    print(g.bfs(0))
    print(g.dfs(0))
    g.print_graph()