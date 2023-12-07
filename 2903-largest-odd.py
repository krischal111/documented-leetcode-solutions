odd = {'1', '3', '5', '7', '9'}
class Solution:
    def largestOddNumber(self, num: str) -> str:
        last = 0
        for i,l in enumerate(num[::-1]):
            if l in odd:
                last = len(num) - i
                break
        return num[:last]