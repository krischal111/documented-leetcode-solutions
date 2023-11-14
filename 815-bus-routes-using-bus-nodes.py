class BusRoutes:
    def __init__(self, routes):
        self.bus_routes = [set(route) for route in routes]
        self.len = len(self.bus_routes)
        self.bus_adjacent_list = {i:[] for i in range(self.len)}
        for i in range(self.len):
            for j in range(i+1, self.len):
                if self.bus_routes[i] & self.bus_routes[j]:
                    self.bus_adjacent_list[i].append(j)
                    self.bus_adjacent_list[j].append(i)
                
    def shortest_path(self, source, target):
        if source == target:
            return 0
        visited_bus = set()
        def bus_of_node(node):
            for i in range(self.len):
                if node in self.bus_routes[i]:
                    yield i
        queue = list(bus_of_node(source))
        target_buses = set(bus_of_node(target))
            
        count = 0
        while queue:
            nextqueue = []
            count += 1
            for bus in queue:
                if bus in visited_bus:
                    continue
                visited_bus.add(bus)

                if bus in target_buses:
                    return count
                
                for next_bus in self.bus_adjacent_list[bus]:
                    if next_bus in visited_bus:
                        continue

                    # if bus in target_buses:
                    #     return count+1
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
                        
