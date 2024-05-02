class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):
            x=i
            for j in range(i,len(nums)):
                if nums[x]<nums[j]:
                    x=j

            temp=nums[i]
            nums[i]=nums[x]
            nums[x]=temp
        nums.reverse()   
        return nums


        
