class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        # now we can move towards the last list, popping away the empty ones
        nums.reverse()
        for i in range(len(nums)):
            # now we can just pop the last element
            nums[i].reverse()

        # always starts at the last
        # each time time starting a step higher
        start = len(nums)-1
        while nums:
            if start == -1:
                start = 0
            i = start
            while True:
                if nums[i]:
                    num = nums[i].pop()
                    yield num
                    i += 1 # index of list to be accessed next
                else:
                    # popping away the empty list
                    # same index will be used for upcoming list
                    nums.pop(i)

                # i always go towards last, until exhaustion
                if i >= len(nums):
                    break
            # next time start a step higher
            start -= 1
            

print("Hello")
mylist = [ans for ans in Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])]
print(mylist)