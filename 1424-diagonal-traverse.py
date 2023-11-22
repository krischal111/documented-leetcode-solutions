class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        l = [(x+y, -y, val) for y, minilist in enumerate(nums) for x, val in enumerate(minilist)]
        l.sort()
        for _, _, val in l:
            yield val

        # return [val for _, _, val in l]
