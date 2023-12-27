class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        repeats = []
        i = 0
        oldc = None
        this_repeat = []
        for c in colors:
            if oldc == c:
                if this_repeat:
                    this_repeat.append(i)
                else:
                    this_repeat = [i-1, i]
            else:
                if this_repeat:
                    repeats.append(list(this_repeat))
                    this_repeat = None
            oldc = c    
            i += 1
        if this_repeat:
            repeats.append(list(this_repeat))
            this_repeat = None
        
        # print(repeats)
        times = [[neededTime[index] for index in indices] for indices in repeats]
        # print(times)
        
        return sum(sum(time) - max(time) for time in times)

                    
        