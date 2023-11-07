import numpy as np
class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        distances = np.array(dist)
        speeds = np.array(speed)
        time = distances / speeds
        l = len(dist)
        sorted_then_remaining_time = np.sort(time) - np.arange(l)
        for i, v in enumerate(sorted_then_remaining_time):
            if v <= 0:
                return i
        else:
            return l
        