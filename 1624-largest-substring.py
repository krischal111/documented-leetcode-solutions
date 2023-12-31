class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_start = {}
        char_end = {}
        for i, c in enumerate(s):
            if c not in char_start:
                char_start[c] = i
            else:
                char_end[c] = i
        # print(char_start)
        # print(char_end)
        # print(dir(char_end))
        if not char_end:
            return -1
        return max(char_end[c] - char_start[c] - 1 for c in char_end)