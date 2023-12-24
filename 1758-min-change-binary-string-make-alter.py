class Solution:
    def minOperations(self, s: str) -> int:
        match = sum(1 for c in s[0::2] if c=='1') + sum(1 for c in s[1::2] if c == '0')
        return min(match, len(s) - match)
        