from collections import Counter

class Solution:
    """
    First Solution
    """
    def majorityElement(self, nums: list[int]) -> int:
        n_count = Counter()
        target = len(nums) // 2
        for n in nums:
            n_count[n] += 1
            if n_count[n] > target:
                return n

class Solution2:
    """
    Follow up
    O(n), O(1)
    """
    def majorityElement(self, nums: list[int]) -> int:
        res, count = nums[0], 1
        for n in nums[1:]:
            count += 1 if n == res else -1
            if count < 0:
                res = n
                count = 0
        return res
