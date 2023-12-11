class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l = 0.25 * len(arr)
        count = 0
        elem = None
        for element in arr:
            if elem == element:
                count += 1
            else:
                count = 1
                elem = element
            if count > l:
                return elem
        