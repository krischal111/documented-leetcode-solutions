import numpy
class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        nums = numpy.array(nums)
        forward_cumsum = numpy.cumsum(nums)
        forward_cumsum = numpy.insert(forward_cumsum,0, 0)
        
        reverse_cumsum = numpy.cumsum(nums[::-1])
        reverse_cumsum = numpy.flip(reverse_cumsum)

        # print(forward_cumsum)
        # print(reverse_cumsum)
        
        n = len(nums)
        ans = []
        for i,num in enumerate(nums):
            value = (2*i - n) * num - forward_cumsum[i] + reverse_cumsum[i]
            yield value
            # ans.append(value)
        # return ans

s = Solution()
answer = s.getSumAbsoluteDifferences([2,3,5])
print(answer);
print([4,3,5], " expected")