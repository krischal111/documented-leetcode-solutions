import numpy as np
class Solution:
    def trap(self, height: list[int]) -> (int, int):
        def my_trap(height):
            height = np.array(height)
            cumsum_height = np.cumsum(height)
            
            total_stored_water = 0
            i = 0
            old_height = height[i]
            
            for j, this_height in enumerate(height):
                if this_height >= old_height:
                    if j - i > 1:
                        stored_water_content = (j-i-1) * old_height - (cumsum_height[j-1] - cumsum_height[i])
                        total_stored_water += stored_water_content
                    i = j 
                    old_height = this_height
                    
            return total_stored_water, i
       
        forward_ans, limit = my_trap(height)
        limit = len(height) - limit
        height.reverse()
        
        back_ans, _ = my_trap(height[:limit]) 

        ans =  forward_ans + back_ans
        return ans


solution = Solution()
answer = solution.trap([4,2,3])
print(answer)
answer = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(answer)
answer = solution.trap([2,0,2])
print(answer)
