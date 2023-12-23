class Solution:
    def isPathCrossing(self, path: str) -> bool:
        point_set = set()
        point = (0,0)
        def move(point, dir):
            x, y = point
            if dir == 'N':
                return (x,y+1)
            elif  dir == 'S':
                return (x, y-1)
            elif dir == 'E':
                return (x+1, y)
            else:
                return (x-1, y)
        point_set.add(point)
        for direction in path:
            point = move(point, direction)
            if point in point_set:
                return True
            else:
                point_set.add(point)
        return False

        