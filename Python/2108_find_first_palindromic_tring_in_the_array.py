class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            l, r = 0, len(word) - 1
            while word[l] == word[r]:
                if l >= r:
                    return word
                l += 1
                r -= 1
        return ""

sol = Solution()
print(sol.firstPalindrome(["abc","car","ada","racecar","cool"]), "ada")
print(sol.firstPalindrome(["notapalindrome","racecar"]), "racecar")
print(sol.firstPalindrome(["def","ghi"]), "")
