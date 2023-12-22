class Solution:
    def maxScore(self, s: str) -> int:
        count_1 = sum(1 for n in s if n == '1')
        count_0 = 1 if s[0] == '0' else 0
        l = len(s)

        if count_1 == 0 or count_0 == l :
            return l - 1

        # if count0 is 0, count 1 is same, otherwise count0 is 1 and count1 is decreased by 1
        count_1 -= (1 - count_0)
        score = count_0 + count_1
        for ch in s[1:-1]:
            zero_here = ch == '0'

            # if not zero_here:
            #     # count 1 decreases
            #     count_1 -= 0
            # new_score = count_0 + count_1


            if ch == '0':
                # count 1 on left increases
                count_0 += 1
            else:
                # count 1 d
                count_1 -= 1
            new_score = count_0 + count_1
            if new_score > score:
                score = new_score
        return score


        return 5
