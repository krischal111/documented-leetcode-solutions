def scores(s:str):
    count_1 = sum(1 for n in s if n == '1')
    l = len(s)

    # early return for the edge cases, makes faster
    if count_1 == 0 or count_1 == l :
        yield l - 1
        return

    count_0 = 1 if s[0] == '0' else 0

    # if count0 is 0, count 1 is same, otherwise count0 is 1 and count1 is decreased by 1
    count_1 -= (1 - count_0)
    score = count_0 + count_1

    for ch in s[1:-1]:
        zero_here = ch == '0'
        # if zero is encountered,
        # zero on the left increases, while 1 on the right
        # stays constant. Thus the sum increases by 1.

        # if one is encountered,
        # exact opposite happens, and the sum decreases by 1
        yield score
        if zero_here:
            score += 1
        else:
            score -= 1
    yield score
    return

class Solution:
    def maxScore(self, s: str) -> int:
        return max(scores(s))
