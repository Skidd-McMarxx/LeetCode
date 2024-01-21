class Solution:
    def rob(self, nums: list[int]) -> int:
        rob_current, rob_next = 0, 0
        for n in nums:
            rob_current, rob_next = rob_next, max(n + rob_current, rob_next)
        return rob_next
