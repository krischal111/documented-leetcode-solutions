class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        arr.sort()
        max = 1
        prev = max
        for num in arr[1:]:
            if num > max:
                max = max+1

        return max
        