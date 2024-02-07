from collections import defaultdict

class Solution:
    """
    tuple list as key
    """
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(word)
        return list(res.values())

class Solution2:
    """
    sorted word as key
    """
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for word in strs:
            res["".join(sorted(word))].append(word)
        return res.values()
