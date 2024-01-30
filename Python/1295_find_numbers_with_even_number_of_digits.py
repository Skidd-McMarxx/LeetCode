class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                count += 1
        return count

class Solution2:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for n in nums:
            if 9 < n < 100 or 999 < n < 10000 or n == 100000:
                count += 1
        return count
