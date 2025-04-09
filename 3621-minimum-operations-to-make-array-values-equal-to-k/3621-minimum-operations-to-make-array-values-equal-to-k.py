class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        uni = set()
        for i in nums:
            if i < k:
                return -1
            elif i == k:
                pass
            else:
                uni.add(i)
        return len(uni)