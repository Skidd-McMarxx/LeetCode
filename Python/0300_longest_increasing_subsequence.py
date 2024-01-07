class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tmp = []

        def binary_search(tmp:list, n:int):
            left, right = 0, len(tmp) - 1
            while left <= right:
                mid = (left + right) // 2
                if tmp[mid] == n:
                    return mid
                elif tmp[mid] < n:
                    left = mid + 1
                elif tmp[mid] > n:
                    right = mid - 1
            return left 
        
        for n in nums:
            if not tmp or tmp[-1] < n:
                tmp.append(n)
            else:
                index = binary_search(tmp, n)
                tmp[index] = n
        return len(tmp)