# from bisect import insort
import bisect

class SeatManager:

    def __init__(self, n: int):
        self.holes = [1]

    def reserve(self) -> int:
        i = self.holes.pop(0)
        if len(self.holes) == 0:
            self.holes.append(i+1)
        return i

    def unreserve(self, seatNumber: int) -> None:
        bisect.insort(self.holes, seatNumber)
        

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)