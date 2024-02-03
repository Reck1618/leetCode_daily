"""
Implement a Weighted Graph.
"""

class Node:
    def __init__(self, key):
        self.val = key
        self.adjacent = {}

    def add_neighbor(self, neighbor, weight = 0):
        self.adjacent[neighbor.val] = weight

    def get_connections(self):
        return self.adjacent.items()

    def get_weight(self, neighbor):
        return self.adjacent.get(neighbor.val, 0)

    def __str__(self):
        return f"Node({self.val}, adjacent: {list(self.adjacent.keys())})"


class Graph:
    def __init__(self):
        self.nodes = {}
        self.num_nodes = 0

    def add_node(self, key):
        if key not in self.nodes:
            self.num_nodes += 1
            new_node = Node(key)
            self.nodes[key] = new_node
            return new_node
        else:
            return self.nodes[key]

    def add_edge(self, from_node, to_node, weight=0):
        # Use add_node method to ensure nodes exist in the graph
        from_node_obj = self.add_node(from_node)
        to_node_obj = self.add_node(to_node)

        if from_node_obj and to_node_obj:  # Check if both nodes were added (not None)
            from_node_obj.add_neighbor(to_node_obj, weight)
            to_node_obj.add_neighbor(from_node_obj, weight)

    def remove_node(self, key):
        pass

    def remove_edge(self, from_node, to_node):
        pass

    def get_node(self, key):
        return self.nodes.get(key, None)

    def get_nodes(self):
        return list(self.nodes.keys())  # Convert keys to list for consistent result

    def __iter__(self):
        return iter(self.nodes.values())


# Creating a graph and adding nodes
graph = Graph()
node1 = graph.add_node(1)
node2 = graph.add_node(2)
node3 = graph.add_node(3)
node4 = graph.add_node(4)

print("Nodes :", graph.get_nodes())

# Adding edges between nodes
graph.add_edge(1, 2, 5)
graph.add_edge(2, 3, 7)
graph.add_edge(3, 1, 3)
graph.add_edge(1, 4, 1)

print("Nodes :", graph.get_node(1))

# Print the nodes and their connections
for node_key in graph.get_nodes():
    node = graph.get_node(node_key)
    connections = node.get_connections()
    print(f"Node {node_key} is connected to nodes and weights: {list(connections)}")


# Accessing specific edge weights
weight_1_to_2 = graph.get_node(1).get_weight(graph.get_node(2))
weight_2_to_3 = graph.get_node(2).get_weight(graph.get_node(3))
weight_3_to_1 = graph.get_node(3).get_weight(graph.get_node(1))

print(f"Weight from Node 1 to Node 2: {weight_1_to_2}")
print(f"Weight from Node 2 to Node 3: {weight_2_to_3}")
print(f"Weight from Node 3 to Node 1: {weight_3_to_1}")
