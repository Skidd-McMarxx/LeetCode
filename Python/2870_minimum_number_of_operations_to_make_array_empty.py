class Solution(object):
    def minOperations(self, nums:list[int]) -> int:
        nums_count = {}
        for n in nums:
            nums_count[n] = nums_count.get(n, 0) + 1
        res = 0
        for n in nums_count:
            if nums_count[n] == 1:
                return -1        
            res += int(-(-(nums_count[n] / 3) // 1))  
        return res