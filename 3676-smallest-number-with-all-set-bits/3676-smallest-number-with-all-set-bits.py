class Solution:
    def smallestNumber(self, n: int) -> int:
        
        
        return (int(len(str(bin(n)[2:]))*"1", 2))