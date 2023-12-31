class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1:
            return True
        
        l = len(words)
        m = sum(map(len, words))

        if m % l != 0:
            return False

        char_count = {}
        for word in words:
            for letter in word:
                if letter in char_count:
                    char_count[letter] += 1
                else:
                    char_count[letter] = 1
        # print(char_count)
        for value in char_count.values():
            if value % (l) != 0:
                return False
        return True
