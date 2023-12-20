# acem cp qustion
# number of ways getting sum of 32 using a 9-sided dice
from pprint import pprint

# for upto 9 case, it's easy

sums = [2**(i-1) for i in range(0,10)]
pprint(sums[1:])



for i in range(10, 33):
    new_sum = 0
    for j in range(1, 10):
        new_sum += sums[i-j]
    pprint(new_sum)
    sums.append(new_sum)

ans = sums[-1]
print(ans)