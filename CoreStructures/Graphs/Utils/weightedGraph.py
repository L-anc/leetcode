from .node import Node

class WeightedGraph:
    def __init__(self, sourceId : int, edges : list[list[int, int, int]]):
        self.nodes = {}
        self.start = sourceId
        for edge in edges:
            node1Id, node2Id, weight = edge
            if node1Id not in self.nodes:
                self.nodes[node1Id] = Node(node1Id, [])
            if node2Id not in self.nodes:
                self.nodes[node2Id] = Node(node2Id, [])
            
            node1 = self.nodes[node1Id]
            node2 = self.nodes[node2Id]

            node1.next.append([node2, weight])
            node2.next.append([node1, weight])
        
        self.start = self.nodes[sourceId]