class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows-1):
            for j in range(i+1,cols):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(rows):
            matrix[i]=matrix[i][::-1]
        return matrix      