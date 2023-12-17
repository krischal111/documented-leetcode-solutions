class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [s for s in s]
        t = [t for t in t]
        s.sort()
        t.sort()
        return s == t
        