class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        my_list = sorted(i for i, j in points)
        my_max = 0
        last_point = my_list[0]
        for this_point in my_list[1:]:
            gap = this_point - last_point
            if gap > my_max:
                my_max = gap
            last_point = this_point
        return my_max
        