class Graph:
    def __init__(self, routes):
        self.adj_list = {}
    def add_route(self, route):
        circuit = set(route)
        for point in circuit:
            next_nodes = set(circuit)
            next_nodes.remove(point)
            if point not in self.adj_list:
                self.adj_list[point] = next_nodes
            else:
                myset = self.adj_list[point]
                myset = myset.unioin(next_nodes)
                
import heapq
class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        my_routes = [set(route) for route in routes]
        visited = set()
        queue = [(0, source)]
        while queue:
            distance, node = heapq.heappop(queue)
            if node == target:
                return distance
            visited.add(node)
            for route in routes:
                if node in route:
                    for next_node in route:
                        if next_node in visited:
                            continue
                        new_dist = 1 + distance
                        heapq.heappush(queue, (new_dist, next_node))
        
        return -1
                        
