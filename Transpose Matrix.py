class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ls=[]
        for i in range(len(matrix[0])):
            ls1=[]
            for j in range(len(matrix)):
                ls1.append(matrix[j][i])
            ls.append(ls1)

        return ls


