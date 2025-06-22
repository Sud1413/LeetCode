class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        j = 0
        if len(s) % k != 0:
            s+=(k - (len(s) % k)) *fill

        for i in range(k,len(s)+1,k):
            ans.append(s[j:i])
            j = i
        
        return ans
