modulo = 10**9 + 7
def rev(num):
    return int(str(num)[::-1])

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        map = {}
        for i in range(len(nums)):
            n = nums[i]
            n -= rev(n)
            # nums[i] = n
            if n in map:
                map[n] += 1
            else:
                map[n] = 1
        total = 0
        for x in map.values():
            total += (((x-1) * (x)) // 2)
        return total%modulo
        