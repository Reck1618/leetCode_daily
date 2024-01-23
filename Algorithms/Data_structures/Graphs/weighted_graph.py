"""
Implement a Graph.
"""

class Node:
    def __init__(self, key):
        self.val = key
        self.adjacent = {}

    def add_neighbor(self, neighbor, weight = 0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

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
            return None  # Return None if the node with the given key already exists

    def get_node(self, key):
        return self.nodes.get(key)

    def add_edge(self, from_node, to_node, weight=0):
        # Use add_node method to ensure nodes exist in the graph
        from_node_obj = self.add_node(from_node)
        to_node_obj = self.add_node(to_node)

        if from_node_obj and to_node_obj:  # Check if both nodes were added (not None)
            from_node_obj.add_neighbor(to_node_obj, weight)

    def get_nodes(self):
        return list(self.nodes.keys())  # Convert keys to list for consistent result

    def __iter__(self):
        return iter(self.nodes.values())
