from collections import deque

class Solution:
    """
    Queue Method
    """
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        res = []
        pos_num, neg_num = deque(), deque()
        for n in nums:
            if n < 0:
                neg_num.append(n)
            elif n > 0:
                pos_num.append(n)
        while pos_num and neg_num:
            res.append(pos_num.popleft())
            res.append(neg_num.popleft())
        return res

class Solution2:
    """
    Two Pointer Method
    """
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums)
        pos_index, neg_index = 0, 1
        for n in nums:
            if n > 0:
                res[pos_index] = n
                pos_index += 2
            else:
                res[neg_index] = n
                neg_index += 2
        return res
