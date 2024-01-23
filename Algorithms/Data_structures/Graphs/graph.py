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

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            self.nodes[node1].discard(node2)
            self.nodes[node2].discard(node1)

    def remove_node(self, key):
        if key in self.nodes:
            # Remove all edges to the node
            for node in self.nodes[key]:
                self.nodes[node].remove(key)

            # Remove the node itself
            del self.nodes[key]


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
