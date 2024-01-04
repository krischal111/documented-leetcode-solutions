from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def from_count(n):
            if n == 1:
                throw -1
            if n % 3 == 0:
                return n//3
            elif n % 3 == 1:
                return (n-4)//3 + 2
            elif n % 3 == 2:
                return (n-2)//3 + 1
        s = 0
        for count in Counter(nums).values():
            try:
                s += from_count(count)
            except:
                return -1
        return s
            

        