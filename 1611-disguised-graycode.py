class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        result = n
        while n:
            n >>= 1
            result ^= n
        return result
        