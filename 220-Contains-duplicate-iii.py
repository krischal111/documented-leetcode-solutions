from sortedcontainers import SortedList
class Solution:
    def 1containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        numlength = len(nums)
        if indexDiff >= numlength:
            indexDiff = numlength-1
        j = indexDiff + 1
        
        sublist = SortedList[:indexDiff]
        for addn in nums[indexDiff:]:
            cmpr = sublist.pop(0)
            sublist.append(addn)
            for num in sublist:
                if -valueDiff <= num - cmpr <= valueDiff:
                    return True
        
        while len(sublist) > 0:
            cmpr = sublist.pop(0)
            for num in sublist:
                if -valueDiff <= num - cmpr <= valueDiff:
                    return True
        
        return False
    

    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        l = len(nums)
        if indexDiff >= l:
            indexDiff = l - 1
        
        slist = SortedList(nums:)



