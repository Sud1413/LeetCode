class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        ans = []

        for i in range(k):
            j = max(nums)
            dict1[nums.index(j)] = j
            nums[nums.index(j)] = -100001

        for k in range(len(dict1)):
            z = min(dict1)
            ans.append(dict1[z])
            del dict1[z]

        return ans