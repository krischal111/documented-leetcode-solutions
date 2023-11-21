class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        M = 0
        P = 0
        G = 0
        total = 0
        for i in range(len(travel)):
            total += travel[i]
            travel[i] = total
        travel.insert(0, 0)
        total = 0
        for i, gbg in enumerate(garbage):
            my_garbage = list(gbg)
            total += len(my_garbage)
            if 'M' in my_garbage:
                M = i
            if 'P' in my_garbage:
                P = i
            if 'G' in my_garbage:
                G = i
        return total + travel[M] + travel[P] + travel[G]