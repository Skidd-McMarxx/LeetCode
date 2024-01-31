class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i, n in enumerate(nums):
            if n != val:
                if k != i:
                    nums[k] = nums[i]
                k += 1
        return k
