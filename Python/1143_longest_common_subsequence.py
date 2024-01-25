from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @cache
        def find_next(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + find_next(i + 1, j + 1)
            return max(find_next(i + 1, j), find_next(i, j+1))

        return find_next(0,0)
