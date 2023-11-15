class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # for eg if I have "*** a bcdef a ***" string, then I have 5 unique palindromes.
        # So I can just count number of unique letters between same letters
        
        unique_letters_between_same_letters = {}
        all_letters = set(s)
        inv_s = s[::-1]
        mylen = len(s)
        
        for l in all_letters:
            i = s.find(l)
            j = inv_s.find(l)
            end = mylen - j
            if end-i != 1:
                unique_letters_between_same_letters[l] = set(s[i+1:end-1])
        

        s = sum(map(len, unique_letters_between_same_letters.values()))
        return s
        # print(unique_letters_between_same_letters)
        # print(s)

Solution().countPalindromicSubsequence("aabca")
Solution().countPalindromicSubsequence("adc")
Solution().countPalindromicSubsequence("bbcbaba")