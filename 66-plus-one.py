class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        d = None
        for i in reversed(range(len(digits))):
            d = digits[i]
            d = (d+1) % 10
            digits[i] = d
            if d != 0:
                break
        if d == 0:
            digits.insert(0, 1)
        return digits

s = Solution()
ans = s.plusOne([1, 2, 3])
print(ans)