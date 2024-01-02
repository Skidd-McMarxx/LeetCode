class Solution(object):
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        seen = {}
        seen[nums[0]] = 0
        for index in range(1, len(nums)):
            for seen_num in seen:
                if nums[index] + seen_num == target:
                    return [seen[seen_num], index]
            seen[nums[index]] = index
