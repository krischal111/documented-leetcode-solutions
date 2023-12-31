class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # bottom up approach
        jobs = len(jobDifficulty)

        if jobs < d:
           return -1
           # cannot be completed
        
        dp = [[0]*jobs]*d
        dp[0][0] = jobDifficulty[0]
        for i in range(1, jobs):
            dp[0][i] =  max(dp[0][i-1], jobDifficulty[i])
        
        for days in range(1, d):
            for i in range(days, jobs):
                this_max = jobDifficulty[i]
                dp[days][i] = 1000

                # j = i
                # while j >= days:
                for j in range(i, days-1, -1):
                    this_max = max(this_max, jobDifficulty[j])
                    dp[days][i] = min(dp[days][i], dp[days-1][j-1] + this_max)
                    # at last
                    # j -= 1
        # print(dp)
        return dp[d-1][jobs-1]

