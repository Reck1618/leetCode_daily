"""
Implement a Graph.
"""

class SimpleGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, key):
        if key not in self.nodes:
            self.nodes[key] = set()

    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)

        # For an undirected graph, add edges in both directions
        self.nodes[node1].add(node2)
        self.nodes[node2].add(node1)

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
