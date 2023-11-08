class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if (sx, sy) == (fx, fy):
            return t != 1
        
        m = max(abs(fx-sx), abs(fy-sy))
        return m <= t;
        