class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if ans < (nums[j] - nums[i]) and (nums[i] != nums[j]):
                    ans = nums[j] - nums[i]
        return ans