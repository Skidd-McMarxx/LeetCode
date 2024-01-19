class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        for ri in range(1, len(matrix)):
            for ci in range(len(matrix)):
                matrix[ri][ci] += min(
                    matrix[ri - 1][ci - 1] if ci != 0 else float("inf"),
                    matrix[ri - 1][ci],
                    matrix[ri - 1][ci + 1] if ci != len(matrix) - 1 else float("inf")
                )
        return min(matrix[-1])