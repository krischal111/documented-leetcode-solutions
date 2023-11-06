from collections import deque
class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        win_count = {num:0 for num in arr}
        l = len(arr)
        k = min(k, l)

        # arr = deque(arr)
        while True:
            a = arr[0]
            b = arr[1]
            # a, b = arr[:2]
            if a > b:
                c = win_count[a]
                c += 1
                win_count[a] = c
                if c == k:
                    return a
                win_count[b] = 0
                arr.append(b)
                arr.pop(1)
                # print(a, "won", win_count)
            else:
                c = win_count[b]
                c += 1
                win_count[b] = c
                if c == k:
                    return b
                win_count[a] = 0
                arr.append(a)
                arr.pop(0)
                # print(b, "won", win_count)
                


answer = Solution().getWinner(arr = [2,1,3,5,4,6,7], k = 2)
print(answer)