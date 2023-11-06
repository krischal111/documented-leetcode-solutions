def permutation_two(p, q):
    n = p + q
    pr = 1
    for i in range(q+1, n+1):
        pr *= i
        if p and pr % p == 0:
            pr //= p
            p -= 1
    return pr

class Solution:
    def climbStairs(self, n: int) -> int:
        def bigyan(np):
            return n - 2 * np
        np = n//2
        perm = 0
        for p in range(np+1):
            q = bigyan(p)
            # print(p, q)
            perm += permutation_two(p, q)
            
        return perm
            
# print(permutation_two(1, 1))
# Solution().climbStairs(2)
        
'''
5 = 2 x 2, 1 x 1
  = 2 x 1, 1 x 3
  = 2 x 0, 1 x 5

5 / 2 = 2
    .. 2, 1, 0,
    2 x 2, 1 x 1 
    1 x 2, 3 x 1
    0 x 2, 5 x 1
    
    P(p, q) =   (p + q)!/ (p! q!)
            =   
'''