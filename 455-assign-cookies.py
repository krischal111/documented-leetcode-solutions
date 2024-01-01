class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        cookie_size = iter(s)
        for greed in g:
            try:
                size = next(cookie_size)
                while size < greed:
                    # print(greed, size)
                    size = next(cookie_size)
            except StopIteration:
                break
            count += 1

        return count
