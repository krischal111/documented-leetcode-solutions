class SeatManager:

    def __init__(self, n: int):
        self.reservations = set()

    def reserve(self) -> int:
        i = 0
        while True:
            i += 1
            if i not in self.reservations:
                self.reservations.add(i)
                return i

    def unreserve(self, seatNumber: int) -> None:
        self.reservations.remove(seatNumber)
        

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)