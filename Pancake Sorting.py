class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n=len(arr)
        ans=[]
        for i in range(n,1,-1):
            ind=arr.index(i)
            arr[:ind+1]=reversed(arr[:ind+1])
            ans.append(ind+1)
            arr[:i]=reversed(arr[:i])
            ans.append(i)
        return ans
