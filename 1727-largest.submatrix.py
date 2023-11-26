import numpy as np
class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        # preprocess
        matrix = np.array(matrix)
        prev_row = np.zeros(matrix.shape[1], dtype=np.int64)
        area = 0
        for row in matrix:
            row += prev_row * row
            prev_row = row
            reverse_sorted_row = sorted(row, reverse=True)

            for j, data in enumerate(reverse_sorted_row):
                if data:
                    area = max(area, (j+1)*data)
                else:
                    break
        return int(area)

# Logic:
# First, for each row, for each data, if it is 1, if it is added to any value above it, if it is zero, kept as it is
# It will transform the matrix as
# 0 0 1
# 1 1 1
# 1 0 1
#  after transformation:
# 0 0 1
# 1 1 2
# 2 0 3
#
# We are counting the continuations of values in that column that way
# From this, just looking at any row, we can see, how much 1's in each columns have appeared.
# Now, sort in reverse order (descending) each rows
# 1 0 0
# 2 1 1
# 3 2 0
#
# We are using position to know how frequent is the repitition.
# We can see, highest continuations of columns are least frequent and are put at the beginning by sorting them
# We can see, for height of 3, there is only one column, but for height of 2, there are two columns
# Now, for each row, we can use the position (1-indexed) as the width, and continuation count as height to calculate area
# We can calculate the maximum area from this


s = Solution()
answer = s.largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]])
# answer = s.largestSubmatrix([[1,0,1,0,1]])
# answer = s.largestSubmatrix([[1,1,0],[1,0,1]])
# answer = s.largestSubmatrix([[0,0],[0,0]])
print(answer)