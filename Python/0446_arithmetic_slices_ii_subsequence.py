class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        output, nums_length = 0, len(nums)
        diff_map = [{} for _ in range(nums_length)] 

        for index in range(nums_length):
            for past_index in range(index):
                diff = nums[index] - nums[past_index]
                if diff not in diff_map[index]:
                    diff_map[index][diff] = 0
                diff_map[index][diff] += diff_map[past_index].get(diff, 0) + 1
                output += diff_map[past_index].get(diff, 0)

        return output
