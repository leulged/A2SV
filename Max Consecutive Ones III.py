class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        maxl = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k -= 1
            while k < 0:  
                if nums[l] == 0:
                    k += 1  
                l += 1
            maxl = max(maxl, i - l + 1)
        return maxl
