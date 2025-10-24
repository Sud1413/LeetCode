class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        while len(s)> 2:
            ans = ""
            for i in range(len(s)-1):
                ans += str((int(s[i]) +int(s[i+1]))%10)

            s = ans
        if s[0] == s[1]:
            return True

        else:
            return False