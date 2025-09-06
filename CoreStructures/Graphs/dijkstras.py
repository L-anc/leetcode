from Utils.weightedGraph import WeightedGraph
from queue import PriorityQueue as PQ
import heapq

def dijkstra(graph):
    node = graph.start
    pq = PQ((0, node))
    dist = [float('inf')]*len(graph.nodes)
    dist[0] = 0
    print(dist)
    
    while not pq.empty:
        (cur_path, node) = pq.get()
        print(node)
        for child, path in node.children():
            print(child)
            path += cur_path
            print(path)
            if dist[child.value()] > dist[node.value()] + path:
                dist[child.value()] = dist[node.value()] + path
            pq.put((dist[child.value()], child))

    return dist
    


graph = WeightedGraph(0, [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]])
print(dijkstra(graph))dict