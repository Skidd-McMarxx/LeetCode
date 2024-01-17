from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        arr_count = Counter(arr).values()
        return len(arr_count) == len(set(arr_count))