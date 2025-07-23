class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[:2]
        for i in range(1,len(s)-1):
            if s[i-1] == s[i]:
                if s[i] != s[i+1]:
                    ans += s[i+1]
            else:
                ans += s[i+1]
        return ans