class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        sum1 = 0

        for i in range(low,high+1):
            a = str(i)
            if len(a) % 2 ==0:
                for j in range(len(a)//2):
                    sum1 += int(a[j])
                    sum1 -= int(a[j+len(a)//2])
                if sum1 == 0:
                    ans += 1
                sum1 = 0
        return ans