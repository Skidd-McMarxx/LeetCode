from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        mag = Counter(magazine)
        for char in ransomNote:
            mag[char] -= 1
            if mag[char] < 0:
                return False
        return True

sol = Solution()
print(sol.canConstruct('a', 'b'), False)
print(sol.canConstruct('aa', 'ab'), False)
print(sol.canConstruct('aa', 'aab'), True)
