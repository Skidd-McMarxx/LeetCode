from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        delta = defaultdict(int)
        for src, per in trust:
            delta[src] -= 1
            delta[per] += 1
        for i in range(1, n + 1):
            if delta[i] == n - 1:
                return i
        return - 1
