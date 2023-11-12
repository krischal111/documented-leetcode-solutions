def find(pair, num):
    a, b = pair
    if a == num:
        return b
    elif b == num:
        return a
    else:
        return None
    

from collections import deque
class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        flattened = [x for minilist in adjacentPairs for x in minilist]

        # creation of adjacency list
        mymap = {}
        for x,y in adjacentPairs:
            if y in mymap:
                mymap[y].append(x)
            else:
                mymap[y] = [x]
            if x in mymap:
                mymap[x].append(y)
            else:
                mymap[x] = [y]
        
        # finding first element of the set
        first = None
        for key, value in mymap.items():
            if len(value) == 1:
                first = key
                break
        
        # print(mymap, first)
        
        visited = set()
        array = []
        stack = [first]
        while len(stack):
            node = stack.pop()

            # extend array and mark the node as visited
            array.append(node)
            visited.add(node)

            next_nodes = mymap[node]
            #add non visited children
            for n in next_nodes:
                if n not in visited:
                    stack.append(n)

        # print(array)
        return array
            
        #     if node not in visited:
        #         node do something
        #         for all nodes add them to stack
        #             them are popped on the next iteration
                

if __name__ == "__main__":
    ans = Solution().restoreArray([[2,1],[3,4],[3,2]])
    ans = Solution().restoreArray([[4,-2],[1,4],[-3,1]])
    print(ans)