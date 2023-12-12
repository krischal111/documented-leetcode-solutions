# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         a, b = sorted(nums)[-2:]
#         print(a,b)
#         return (a-1)*(b-1)

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        a, b = nums[:2]
        a, b = (a,b) if a <= b else (b, a)
        for num in nums[2:]:
            if num >= b:
                a = b
                b = num
            elif num >= a:
                a = num

        return (a-1)*(b-1)