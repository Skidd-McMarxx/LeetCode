class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        targ_nums = set()
        for n in arr:
            if n in targ_nums:
                return True
            if n % 2 == 0:
                targ_nums.add(n // 2)
            targ_nums.add(n * 2)
        return False
