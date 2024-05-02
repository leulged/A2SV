class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        print(piles)
        x = 0
        start = int(n/3) 
        while start < n:
            x += piles[start]
            start += 2
        return x
