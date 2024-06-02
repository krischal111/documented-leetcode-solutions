class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        reverselist = list(reversed(s))
        for i, char in enumerate(reverselist):
            s[i] = char
        
        
    def reverseString2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        lptr = 0
        while lptr < l - lptr:
            s[lptr], s[-lptr-1] = s[-lptr-1], s[lptr]
            lptr += 1
        
    