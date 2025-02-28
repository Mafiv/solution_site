# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:  # Handle empty matrix case
            self.mat = []
            return
        rows, cols = len(matrix), len(matrix[0])
        self.mat = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                self.mat[i][j] = matrix[i][j]
                if j > 0:
                    self.mat[i][j] += self.mat[i][j - 1]
                if i > 0:
                    self.mat[i][j] += self.mat[i - 1][j]
                if i > 0 and j > 0:
                    self.mat[i][j] -= self.mat[i - 1][j - 1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.mat[row2][col2]
        if col1 > 0:
            total -= self.mat[row2][col1 - 1]
        if row1 > 0:
            total -= self.mat[row1 - 1][col2]
        if row1 > 0 and col1 > 0:
            total += self.mat[row1 - 1][col1 - 1]
        return total



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)