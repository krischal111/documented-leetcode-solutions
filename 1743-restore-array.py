def find(pair, num):
    a, b = pair
    if a == num:
        return b
    elif b == num:
        return a
    else:
        return None
    

class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        mylist = adjacentPairs.pop()
        l, r = mylist
        i = len(adjacentPairs)-1
        # j = 0
        while adjacentPairs:
            # j += 1
            # if j > 10:
            #     return
            # print(l, mylist, r, adjacentPairs[i], "from", adjacentPairs)
            num = find(adjacentPairs[i], l)
            if num is not None:
                mylist.insert(0, num)
                adjacentPairs.pop(i)
                l = num
                num = None
            else:
                num = find(adjacentPairs[i], r)
                
            if num is not None:
                mylist.append(num)
                r = num
                adjacentPairs.pop(i)
            
            i -= 1
            if i < 0:
                ll = len(adjacentPairs)
                if ll == 0:
                    break
                i %= ll
        
        return mylist
            
        
if __name__ == "__main__":
    ans = Solution().restoreArray([[2,1],[3,4],[3,2]])
    ans = Solution().restoreArray([[4,-2],[1,4],[-3,1]])
    print(ans)