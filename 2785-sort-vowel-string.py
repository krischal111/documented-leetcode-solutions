# import heapq

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        my_vowels = []
        my_positions = set()
        for i, l in enumerate(s):
            if l in vowels:
                my_positions.add(i)
                my_vowels.append(l)

        my_vowels.sort()
        
        ans = []
        for i, j in enumerate(s):
            if i in my_positions:
                ans.append(my_vowels.pop(0))
            else:
                ans.append(j)
        
        return ''.join(ans)
        
        
        

                