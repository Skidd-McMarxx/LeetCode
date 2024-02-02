from collections import deque


class Solution:
    """
    Generate numbers
    """
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        seq = deque(range(1,10))
        res = []
        while seq:
            n = seq.popleft()
            if n > high:
                return res
            if low <= n <= high:
                res.append(n)
            ones_unit = n % 10
            if ones_unit < 9:
                seq.append(n * 10 + ones_unit + 1)
        return res

class Solution2:
    """
    All the numbers
    """
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        possible_seq = [12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,
                        1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,
                        56789,123456,234567,345678,456789,1234567,2345678,
                        3456789,12345678,23456789,123456789]
        res = []
        for seq in possible_seq:
            if low <= seq <= high:
                res.append(seq)
            elif seq > high:
                return res
        return res
