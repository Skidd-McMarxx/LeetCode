from collections import Counter

# 2 Hash maps
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        return sum((s_count - t_count).values())

# 1 Hash maps
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        count = 0        
        for char in t:
            if char in s_count and s_count[char] > 0:
                s_count[char] -= 1
            else:
                count += 1
        return count