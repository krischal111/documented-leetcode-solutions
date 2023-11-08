class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        # sulto:
        d1 = set()
        d2 = set()
        
        for i, (c1, c2) in enumerate(zip(s1[:-1], s2[:-1])):
            d1.add(c1)
            d2.add(c2)
            if d1 == d2:
                scrambled = True
                s11, s12 = s1[:i+1], s1[i+1:]
                s21, s22 = s2[:i+1], s2[i+1:]
                # print(s11, ' ', s12, i)
                # print(s21, ' ', s22, i)
                scrambled = scrambled and self.isScramble(s11, s21) 
                scrambled = scrambled and self.isScramble(s12, s22)
                if scrambled:
                    print(s11, s12)
                    print(s21, s22)
                    return True
        
        #ulto
        d1 = set()
        d2 = set()
        for i, (c1, c2) in enumerate(zip(s1[:0:-1], s2[:-1])):
            d1.add(c1)
            d2.add(c2)
            if d1 == d2:
                scrambled = True
                s11, s12 = s1[:-i-1], s1[-i-1:]
                s21, s22 = s2[:i+1], s2[i+1:]
                # print("ulto")
                # print(s11, ' ', s12, i)
                # print(s21, ' ', s22, i)
                scrambled = scrambled and self.isScramble(s12, s21) 
                scrambled = scrambled and self.isScramble(s11, s22)
                if scrambled:
                    print(s11, s12)
                    print(s21, s22)
                    return True
        # print(s1, s2, "not scrambled")
        return False
                

cases = [
    ('great', 'rgeat', True), 
    ('abcde', 'caebd', False),
    ("ccabcbabcbabbbbcbb", "bbbbabccccbbbabcba", False)
    ]
        
if __name__ == '__main__':
    for s1, s2, answer in cases:
        ans = Solution().isScramble(s1,s2)
        print(f"Got {ans} : {answer} expected")