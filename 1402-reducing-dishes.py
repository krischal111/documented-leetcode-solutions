class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()
        if satisfaction[-1] <= 0:
            return 0
        sum_satis = sum(satisfaction)
        total_satisfaction_coefficient = sum([s * (i+1) for i, s in enumerate(satisfaction)])
        while True:
            new_satisfaction_coeff = total_satisfaction_coefficient - sum_satis
            if new_satisfaction_coeff >= total_satisfaction_coefficient:
                sum_satis -= satisfaction.pop(0)
                total_satisfaction_coefficient = new_satisfaction_coeff
            else:
                return total_satisfaction_coefficient
        
        