import heapq
class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        my_routes = [set(route) for route in routes]
        visited = set()
        queue = [(0, source, [])]
        while queue:
            distance, node, route = heapq.heappop(queue)
            if node == target:
                return distance
            visited.add(node)
            for bus, route in enumerate(routes):
                if node in route:
                    for next_node in route:
                        if next_node in visited:
                            continue
                        new_dist = 1 + distance
                        new_route = list(route)
                        new_route.append(bus)
                        heapq.heappush(queue, (new_dist, next_node, new_route))
        
        return -1
                        
        