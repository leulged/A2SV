class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ls=[]
        for i in range(len(nums)):
            c=0
            for j in range(len(nums)):
                
                if nums[j] < nums[i] and i!=j:
                    c+=1
            ls.append(c)
        return ls



        
