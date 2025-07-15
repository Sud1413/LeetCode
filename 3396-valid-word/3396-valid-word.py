class Solution:
    def isValid(self, word: str) -> bool:
        ans = True
        vcount = 0
        ccount = 0

        if len(word) < 3:
            ans = False
            return ans

        for i in word:
            if  i.isdigit() or i.isalpha():
                ans = True
            else:
                ans = False
                return ans
            if i.isalpha():
                if i in ["A","a","E","e","I","i","O","o","U","u"]:
                    vcount += 1
                else:
                    ccount += 1
        if vcount > 0 and ccount > 0:
            ans = True
        else:
            ans = False
        return ans
        