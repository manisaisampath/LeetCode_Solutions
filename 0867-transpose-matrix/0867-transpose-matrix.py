class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        mat=[]
        col=len(matrix[0])
        row=len(matrix)
        for j in range(col):
            res=[]
            for i in range(row):
                res.append(matrix[i][j])
            mat.append(res)
        return mat
