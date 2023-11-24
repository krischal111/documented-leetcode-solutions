class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        return sum(sorted(piles)[len(piles)//3::2])
        # piles.sort()
        # l = len(piles) // 3
        # return sum(piles[-2:(l-1):-2])