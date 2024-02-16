from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        freq = [0] * len(arr)
        for _, c in Counter(arr).items():
            freq[c - 1] += 1
        res = sum(freq)
        for f, i in enumerate(freq, 1):
            if k >= f * i:
                k -= f * i
                res -= i
            else:
                remo = k // f
                res -= remo
                break
        return res
    
sol = Solution()
print(sol.findLeastNumOfUniqueInts([5,5,4], 1))
print(sol.findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))
