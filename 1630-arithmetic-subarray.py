class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # ans = []
        for i, j in zip(l,r):
            my_slice = nums[i:j+1]
            my_slice.sort()
            print(my_slice)
            old_element = my_slice[0]
            old_difference = None
            for this_element in my_slice[1:]:
                new_difference = old_element - this_element
                if old_difference is not None:
                    if new_difference != old_difference:
                        # ans.append(False)
                        yield False
                        break
                old_difference = new_difference
                old_element = this_element
            else:
                yield True
                # ans.append(True)
        # return ans