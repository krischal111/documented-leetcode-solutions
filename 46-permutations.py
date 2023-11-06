class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        l = len(nums)
        if l == 1:
            return [nums]
        answer = []
        for i in range(l):
            item = nums[i]
            mylist = list(nums)
            mylist.remove(item)
            mypermut = self.permute(mylist)
            ll = len(mypermut)
            for ii in range(ll):
                mypermut[ii].append(item)
            answer.extend(mypermut)
        return answer

# s = Solution()
# p = s.permute([1, 2, 3])
# print(p)
