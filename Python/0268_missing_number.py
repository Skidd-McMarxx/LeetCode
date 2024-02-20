class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res

sol = Solution()
print(sol.missingNumber([3,0,1]))
