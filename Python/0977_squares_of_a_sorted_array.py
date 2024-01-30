class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for index, n in enumerate(nums):
            nums[index] = n ** 2
        nums.sort()
        return nums

class Solution2:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right, res = 0, len(nums) - 1, []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1
        return res[::-1]
