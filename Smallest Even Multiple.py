class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        import math
        if n%2==0:
            return n
        else:
            return n*2
        
