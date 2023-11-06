class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = 0
        counting = False
        for l in s[::-1]:
            if counting and l != ' ':
                j += 1
            if not counting and l != ' ':
                counting = True
                j += 1
            if counting and l == ' ':
                break
        return j    
                