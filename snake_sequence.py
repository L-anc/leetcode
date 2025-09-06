class directedGraph:
    def __init__(self):
        self.children = {}

    def __init__(self, list):
        

    def add_edge(self, from_node, to_node):
        if from_node not in self.children:
            self.children[from_node] = []
        self.children[from_node].append(to_node)

    def get_edges(self, node):
        return self.children.get(node, [])