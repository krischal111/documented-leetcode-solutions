class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        for i, j in zip(l,r):
            if j - i < 2:
                yield True
                continue
            my_slice = sorted(nums[i:j+1])
            old = my_slice[0]
            middle = my_slice[1]
            for new in my_slice[2:]:
                if middle << 1 != old + new:
                    yield False
                    break
                old = middle
                middle = new
            else:
                yield True