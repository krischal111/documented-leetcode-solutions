class Solution:
    def countHomogenous(self, s: str) -> int:
        # splicing
        def splice(s:str):
            sp = []
            if not s:
                return sp
            prevchar = s[0]
            prevstr = prevchar
            for c in s[1:]:
                if prevchar != c:
                    sp.append(prevstr)
                    prevstr = ""
                    prevchar = c
                prevstr += c
            sp.append(prevstr)
            return sp
        ans = sum(map(lambda x: (x * (x + 1))//2 , [len(s) for s in splice(s)]))
        return ans % (10**9 + 7)
        # return splice(s)
        
if __name__ == '__main__':
    ans = Solution().countHomogenous("abbcccaa")
    print(ans)