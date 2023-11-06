class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int((s.count(letter) * 100) / len(s))

a = Solution()
i = a.percentageLetter("foooor", 'o')
print(i)
