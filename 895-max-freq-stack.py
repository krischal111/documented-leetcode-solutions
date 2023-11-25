import heapq

class FreqStack:
    def __init__(self):
        self.stack = []
        self.len = 0
        self.count = {}

    def push(self, val: int) -> None:
        if val in self.count:
            self.count[val] += 1
        else:
            self.count[val] = 1
        count = self.count[val]
        heapq.heappush(self.stack, ((-count, -self.len), val))
        self.len += 1
        # print(self.stack)
        
    def pop(self) -> int:
        (count, _), val = heapq.heappop(self.stack)
        count += 1
        self.count[val] = -count
        # print(self.stack)
        return val