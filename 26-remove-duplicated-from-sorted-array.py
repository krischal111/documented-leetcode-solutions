class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        done = set()
        indices = []
        l = len(nums)
        k = 0
        for i in range(l):
            d = nums[i]
            if d in done:
                indices.append(i)
            else:
                done.add(d)
                k += 1
        for i in reversed(indices):
            nums.pop(i)
        return k
            

        