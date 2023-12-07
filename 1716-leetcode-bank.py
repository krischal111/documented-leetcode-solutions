def sumn(n):
    return (n * (n-1))//2
class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        for i in range(7):
            count = (n+i)//7
            total += (7-i) * count
            total += sumn(count)
        return total
