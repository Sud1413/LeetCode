class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        ans = 0
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        for j in freq:
            if freq[j] == max(freq.values()):
                ans += freq[j]
        return ans