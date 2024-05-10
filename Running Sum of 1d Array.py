class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cursum=0
        arr=[]
        for i in range(1,len(nums)+1):
            arr.append(sum(nums[:i]))
        return arr

        
