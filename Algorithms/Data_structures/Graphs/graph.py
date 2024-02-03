"""
Implement a Simple Graph.
"""

class SimpleGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, key):
        if key not in self.nodes:
            self.nodes[key] = set()

    def add_edge(self, source, destination):
        self.add_node(source)
        self.add_node(destination)

        # For an undirected graph, add edges in both directions
        self.nodes[source].add(destination)
        # self.nodes[node2].add(node1)

    def remove_edge(self, source, destination):
        if source in self.nodes and destination in self.nodes:
            self.nodes[source].discard(destination)
            # self.nodes[node2].discard(node1)

    def remove_node(self, key):
        if key in self.nodes:
            # Remove all edges to the node
            for node in self.nodes[key]:
                self.nodes[node].remove(key)

            # Remove the node itself
            del self.nodes[key]

    # transpose the graph

    # cycle detection

    # all paths between two nodes

    # shortest path between two nodes

    # topological sort

    # strongly connected components

    # number of nodes at each level


    def are_connected(self, node1, node2):
        return node2 in self.nodes.get(node1, set())

    def print_graph(self):
        for node, neighbors in self.nodes.items():
            print(f"Node {node} is connected to nodes: {list(neighbors)}")


# Test the SimpleGraph
simple_graph = SimpleGraph()
simple_graph.add_edge(1, 2)
simple_graph.add_edge(2, 3)
simple_graph.add_edge(3, 1)
simple_graph.add_edge(3, 4)

simple_graph.print_graph()

# Check if nodes are connected
print(f"Are nodes 1 and 2 connected? {simple_graph.are_connected(1, 2)}")
print(f"Are nodes 1 and 4 connected? {simple_graph.are_connected(1, 4)}")
print(f"Are nodes 1 and 4 connected? {simple_graph.are_connected(2, 4)}")

# Remove an edge
simple_graph.remove_edge(1, 2)
print("Removed edge 1-2")
print(f"Are nodes 1 and 2 connected? {simple_graph.are_connected(1, 2)}")

# Remove a node
simple_graph.remove_node(4)
print("Removed node 4")
simple_graph.print_graph()
