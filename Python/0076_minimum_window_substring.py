from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        t_count = Counter(t)
        s_count = defaultdict(int)
        foun_match, targ_match = 0, len(t_count)
        res, res_len = [0, 0], float('inf')
        l = 0
        for r, num in enumerate(s):
            s_count[num] += 1
            if s_count[num] == t_count[num]:
                foun_match += 1
            while foun_match == targ_match:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                if s_count[s[l]] == t_count[s[l]]:
                    foun_match -= 1
                s_count[s[l]] -= 1
                l += 1
        return s[res[0]:res[1] + 1] if res_len != float('inf') else ""
