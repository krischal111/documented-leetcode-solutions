import numpy as np
from queue import PriorityQueue
import heapq

class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        self.adj_list = np.ones((n,n)) * np.inf
        for node1, node2, weight in edges:
            self.adj_list[node1][node2] = weight

    def addEdge(self, edge: list[int]) -> None:
        node1, node2, weight = edge
        self.adj_list[node1][node2] = weight

    def shortestPath(self, node1: int, node2: int) -> int:
        visited = set()
        p_queue = []
        heapq.heappush(p_queue,(0, node1))
        while p_queue:
            distance, node = heapq.heappop(p_queue)
            # print(f"Visiting node {node} with distance {distance}")
            if node == node2:
                return int(distance)
            visited.add(node)
            for children_node, weight in enumerate(self.adj_list[node]):
                # print(f'here {children_node} with {weight}')
                if np.isinf(weight):
                    # print('continue')
                    continue
                if children_node not in visited:
                    # print(f'putting children {children_node}')
                    dist = weight + distance
                    heapq.heappush(p_queue,(dist, children_node))
        return -1
        

if __name__ == '__main__':
    g = Graph(4,[[0,2,5],[0,1,2],[1,2,1],[3,0,3]])
    path = g.shortestPath(3,2)
    print(path)
    path = g.shortestPath(0,3)
    print(path)
    g.addEdge([1,3,4])


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)