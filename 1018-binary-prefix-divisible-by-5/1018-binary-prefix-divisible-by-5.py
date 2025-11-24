class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        sol = ""


        for i in nums:
            sol += str(i)
            ans.append(int(sol,2)%5==0)
        return ans