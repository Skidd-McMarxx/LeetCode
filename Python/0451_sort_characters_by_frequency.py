from collections import Counter, defaultdict

class Solution:
    """
    Bucket Sorted
    """
    def frequencySort(self, s: str) -> str:
        char_count = Counter(s)
        char_map = defaultdict(list)
        for char, cnt in char_count.items():
            char_map[cnt].append(char)
        res = []
        for i in range(len(s), 0, -1):
            for char in char_map[i]:
                res.append(char * i)
        return "".join(res)

class Solution2:
    """
    Python Counter Method
    """
    def frequencySort(self, s: str) -> str:
        char_count = Counter(s)
        return "".join(char * i for char, i in char_count.most_common())
