# 2 half loops
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count_vowels(half:str) -> int:
            count = 0
            for c in half:
                if c.lower() in ('a','e','i','o','u'):
                    count += 1
            return count
            
        return count_vowels(s[:len(s)//2]) == count_vowels(s[len(s)//2:])

# 2 checks 1 loop
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        left, right = 0,len(s)-1
        while left < right:
            if s[left].lower() in ('a','e','i','o','u'):
                count += 1
            if s[right].lower() in ('a','e','i','o','u'):
                count -= 1
            left += 1
            right += 1 
        return count == 0