# mycount = 0
# class Solution:
#     def getPermutation(self, n: int, k: int) -> str:
#         mylist = list(map(str,range(1,n+1)))
#         # print(mylist)
#         # return

#         # res = []
#         global mycount
#         mycount = 0
#         def increment():
#             global mycount
#             mycount += 1
#         # increment = lambda : (mycount = mycount+1)*0
#         thiscount = lambda : mycount
#         def sth(index, cursor):
#             if index == n:
#                 # res.append(cursor)
#                 increment()
#                 if thiscount() == k:
#                     return cursor
#             for i in mylist:
#                 sth(index+1, cursor+i)
        
#         sth(0,'')
#         return res
        

@cache
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = list(map(str, range(1, n+1)))
        def miniperm(digits, n,k):
            if not n:
                return ""

            dividend = k
            divisor = factorial(n-1)
            quotient, remainder = divmod(dividend, divisor)
            # quotient = dividend // divisor
            # remainder = dividend % divisor
            quotient = quotient if remainder else quotient-1
            digit = digits[quotient]

            deeperdigits = list(digits)
            deeperdigits.remove(digit)
            return digit + miniperm(deeperdigits, n-1, remainder)

        return miniperm(digits, n, k)


        