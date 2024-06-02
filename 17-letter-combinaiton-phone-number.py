map = {
    2:"abc",
    3:"def",
    4:"ghi",
    5:'jkl',
    6:'mno',
    7:'pqrs',
    8:'tuv',
    9:'wxyz',
}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
    
        combinations = list(map[eval(digits[0])])
        for digit in digits[1:]:
            new_combinations = list(map[eval(digit)])
            next_combinations = []
            for old_combin in combinations:
                for new_combin in new_combinations:
                    next_combinations.append(old_combin+new_combin)
            combinations = next_combinations

        # print(combinations)
        return combinations
# exit()

    def letterCombinations_dfs(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        letter_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
                      "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        def backtrack(i, current_str):
            if len(current_str) >= len(digits): # Base case.
                res.append(current_str)
                return
            
            # Loop through every value of current keyand make a recursive call.
            for c in letter_map[digits[i]]:
                backtrack(i + 1, current_str + c)
        
        backtrack(0, "")
        return res

map = {
    2:"abc",
    3:"def",
    4:"ghi",
    5:'jkl',
    6:'mno',
    7:'pqrs',
    8:'tuv',
    9:'wxyz',
}

def letterCombinations1(digits: str) -> List[str]:
    if not digits:
        return []

    res = []
    letter_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
                    "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

    def backtrack(i, current_str):
        if len(current_str) >= len(digits): # Base case.
            res.append(current_str)
            return
        
        # Loop through every value of current keyand make a recursive call.
        for c in letter_map[digits[i]]:
            backtrack(i + 1, current_str + c)
    
    backtrack(0, "")
    return res

with open("user.out", "w") as f:
    for case in stdin:
        f.write(f"{dumps(letterCombinations1(loads(case.strip()))).replace(', ', ',')}\n")
exit()
        