class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = 0

        for i in set(arr):
            if arr.count(i) == i:
                if ans < i:
                    ans = i

        if ans == 0:
            return -1
        else:
            return ans