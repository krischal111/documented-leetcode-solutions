class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        start_set = set()
        end_set = set()
        for start, end in paths:
            start_set.add(start)
            end_set.add(end)
        return (end_set - start_set).pop()
        