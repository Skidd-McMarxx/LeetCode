class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count, output = 0, 0

        for index in range(1, len(nums) -1):
            if nums[index] - nums[index - 1] == nums[index + 1] - nums[index]:
                count += 1
                output += count
            else:
                count = 0
        return output