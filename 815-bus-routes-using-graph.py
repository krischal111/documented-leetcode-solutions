class BusRoutes:
    def __init__(self, routes):
        self.routes = routes
        self.all_nodes = list({node for circuit in routes for node in circuit})
        self.bus_of_node = {node:[] for node in self.all_nodes}
        for node in self.all_nodes:
            for bus, circuit in enumerate(self.routes):
                if node in circuit:
                    self.bus_of_node[node].append(bus)
    
    def shortest_path(self, source, target):
        if source == target:
            return 0
        visited_nodes = set()
        visited_bus = set()
        queue = list(self.bus_of_node[source])
            
        count = 0
        while queue:
            nextqueue = []
            count += 1
            for bus in queue:
                if bus in visited_bus:
                    continue
                visited_bus.add(bus)
                if target in self.route_set[bus]:
                    return count
                for node in self.routes[bus]:
                    if node in visited_nodes:
                        continue
                    visited_nodes.add(node)
                    if node == target:
                        return count
                    for next_bus in self.bus_of_node[node]:
                        if next_bus in visited_bus:
                            continue
                        nextqueue.append(next_bus)
            queue = nextqueue
        return -1
                
from collections import deque
class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = BusRoutes(routes)
        return graph.shortest_path(source, target)
                        
