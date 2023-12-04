# I used regex
import re
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = []

        # we have to match number that are 3 same digit:
        # like 111 or 222 and so

        for word in re.finditer(r"(\d)\1{2}", num):
            # after iterating through the matches using regex
            # we append the captured group to the good list
            good.append(word.group())
        
        if good:
            # from which we return the maximum value
            # if it contains something
            return f"{max(good):3}"
        else:
            # else, we return an empty string
            return ""