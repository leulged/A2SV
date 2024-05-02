class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        res=[[0 for i in range(n-2)] for i in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                b=grid[i+1][j+1]
                for ii in range(i,i+3):
                    for jj in range(j,j+3):
                        b=max(b,grid[ii][jj])
                res[i][j]=b
        return res



