class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        res = -1
        total = nums[0] + nums[1]
        for n in nums[2:]:
            if total > n:
                res = total + n
            total += n
        return res
