import numpy as np
class SeatManager:

    def __init__(self, n: int):
        self.reservations = np.zeros(n, dtype=bool)

    def reserve(self) -> int:
        i = np.where(self.reservations == False)[0][0]
        self.reservations[i] = True
        return i+1

    def unreserve(self, seatNumber: int) -> None:
        self.reservations[seatNumber-1] = False
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)