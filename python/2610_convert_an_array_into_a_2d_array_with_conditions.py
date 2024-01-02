class Solution(object):
    def findMatrix(self, nums:list[int]) -> list[list[int]]:
        counter = {}
        output = []
        for n in nums:
            row_index = counter.get(n, 0)
            if len(output) == row_index:
                output.append([])
            output[row_index].append(n)
            counter[n] = counter.get(n, 0) + 1
        return output    