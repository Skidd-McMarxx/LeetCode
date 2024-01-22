class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        seen = set()
        nums_sum, dup = 0, 0
        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                dup = n
            nums_sum += n
        exp_sum = len(nums) * (len(nums) + 1) // 2
        mis = exp_sum - (nums_sum - dup)
        return [dup, mis]
