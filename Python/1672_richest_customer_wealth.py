class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(sum(cust) for cust in accounts)
