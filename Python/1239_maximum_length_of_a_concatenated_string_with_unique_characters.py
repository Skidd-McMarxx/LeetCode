class Solution:
    def maxLength(self, arr: list[str]) -> int:
        seen_words = [""]
        res= 0
        for word in arr:
            for seen in seen_words:
                con_word = word + seen
                if len(con_word) != len(set(con_word)):
                    continue
                seen_words.append(con_word)
                res = max(res, len(con_word))
        return res