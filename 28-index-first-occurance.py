class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = haystack.find(needle)
        if l is None:
            return -1
        return l
