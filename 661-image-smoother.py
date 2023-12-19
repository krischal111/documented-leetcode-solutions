class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        output = [[0 for _ in range(n)] for _ in range(m)]
        def smooth(i,j):
            sum = 0
            count = 0
            for y in range(i-1, i+2):
                for x in range(j-1, j+2):
                    if 0 <= y < m and 0 <= x < n:
                        count += 1
                        sum += img[y][x]
            output[i][j] = sum//count

        for i in range(m):
            for j in range(n):
                smooth(i,j)

        return output
        