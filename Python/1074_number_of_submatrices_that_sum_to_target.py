from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        sum_map = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for ri, row in enumerate(matrix):
            for ci, num in enumerate(row):
                top = sum_map[ri - 1][ci]
                left = sum_map[ri][ci - 1] 
                top_left = sum_map[ri - 1][ci - 1] if min(ri, ci) > 0 else 0
                sum_map[ri][ci] = num + top + left - top_left

        res = 0
        for rs in range(len(matrix)):
            for re in range(rs, len(matrix)):
                count = defaultdict(int)
                count[0] = 1
                for cs in range(len(matrix[0])):
                    curr = sum_map[re][cs] - (
                        sum_map[rs - 1][cs] if rs > 0 else 0
                    )
                    diff = curr - target
                    res += count[diff]
                    count[curr] += 1
        return res
