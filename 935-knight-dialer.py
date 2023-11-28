next_hops = {
    1:[6,8],
    2:[7,9],
    3:[4,8],
    4:[3,9,0],
    5:[],
    6:[1,7,0],
    7:[2,6],
    8:[1,3],
    9:[4,2],
    0:[4,6]
}
modulo = 10**9 + 7

# Idea:
# Count how many pathways you can go for a certain depth for all numbers
# For 1-depth, each number just has single depth to travel
# For n+1 depth, each number has the path count, that is equal to sum of pathcounts of all numbers it can go for n depth.
# If you do this using recursion, it will take time
# But if you do using dynamic programming, it will become faster

class Solution:
    def knightDialer(self, n: int) -> int:
        dp = {}
        for i in range(10):
            dp[(i,0)] = 1
        for n in range(n):
            for i in range(10):
                dp[(i,n+1)] = sum((dp[(i,n)] for i in next_hops[i])) % modulo
        return sum((dp[i,n] for i in range(10))) % modulo
