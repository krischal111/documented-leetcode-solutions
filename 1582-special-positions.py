class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        row_sum = [sum(row) for row in mat]
        col_sum = [0 for _ in mat[0]]
        
        for i in range(m):
            for j in range(n):
                col_sum[j] += mat[i][j]
        
        count = 0
        for i, row in enumerate(row_sum):
            if row != 1:
                continue
            for j, col in enumerate(col_sum):
                if col == 1 == mat[i][j]:
                    count += 1
                    # print(f"At ({i}, {j})")
        
        return count
                


        