class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = [max(nums)]

        for i in nums:
            if i > 0:
                if i not in ans:
                    ans.append(i)
        return sum(ans)