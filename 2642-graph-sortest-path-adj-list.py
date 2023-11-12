import heapq

class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        # since `n` nodes are from 0 n-1, they can be indexed through list 
        self.adj_list = [ list() for _ in range(n)]
        for edge in edges:
            self.addEdge(edge)
        # print(self.adj_list)

    def addEdge(self, edge: list[int]) -> None:
        node1, node2, weight = edge
        # each node contains the list of neighbouring nodes and their respective weights
        self.adj_list[node1].append((node2, weight))

    def shortestPath(self, node1: int, node2: int) -> int:
        visited = set()

        # The heapified priority queue allows us to select the node with
        # lowest priority, i.e. node with the least distance
        p_queue = []
        heapq.heappush(p_queue,(0, node1))
        while p_queue:
            distance, node = heapq.heappop(p_queue)
            # print(f"Visiting node {node} with distance {distance}")
            if node == node2:
                return int(distance)
            visited.add(node)
            for children_node, weight in self.adj_list[node]:
                if children_node in visited:
                    continue
                dist = weight + distance
                heapq.heappush(p_queue, (dist, children_node))
                
        return -1
        

if __name__ == '__main__':
    task = ["Graph","shortestPath","shortestPath","shortestPath","shortestPath","addEdge","shortestPath","addEdge","shortestPath","shortestPath","addEdge","addEdge","shortestPath","addEdge","addEdge","addEdge","addEdge","shortestPath","shortestPath","addEdge","addEdge","shortestPath","addEdge","addEdge","addEdge","shortestPath","addEdge","shortestPath","shortestPath","shortestPath","shortestPath","addEdge","addEdge"]
    testcase = [[6,[[3,5,990551],[1,3,495721],[0,1,985797],[4,5,422863],[4,1,505663]]],[0,1],[3,5],[4,4],[0,3],[[5,0,250117]],[4,5],[[3,1,142005]],[2,2],[4,0],[[2,0,124744]],[[5,1,74396]],[3,3],[[3,2,571238]],[[1,4,3408]],[[0,4,832]],[[5,2,417]],[2,2],[2,4],[[2,3,80]],[[5,4,6]],[3,4],[[4,3,837171]],[[1,2,162278]],[[3,4,1]],[2,0],[[0,3,1]],[0,4],[3,5],[1,1],[3,4],[[4,2,1]],[[2,1,1]]]
    g = None
    for task, value in zip(task, testcase):
        if task == "Graph":
            n, edges = value
            g = Graph(n, edges)
        elif task == "addEdge":
            value = value.pop()
            # print(f"task {task} {value}")
            # g.addEdge(value.pop())
        else:
            # print(f"task {task} {value}")
            node1, node2 = value
            ans = g.shortestPath(node1, node2)
            print(f"Shortest path from {node1} to {node2} is {ans}")

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)