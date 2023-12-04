import numpy as np
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        points = np.array(points, dtype=np.int32)

        prev = points[0]
        distance = 0

        for point in points[1:]:
            distance += np.max(np.abs(point-prev))
            prev = point
        
        return distance