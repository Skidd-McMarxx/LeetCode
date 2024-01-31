class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Array modified in place
        """
        left, right = len(arr) - 1, len(arr) - 1 + arr.count(0)
        while left < right:
            if right < len(arr):
                arr[right] = arr[left]
            if arr[left] == 0:
                right -= 1
                if right < len(arr):
                    arr[right] = arr[left]
            left -= 1
            right -= 1
        print(arr)

class Solution2:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Array changes sizes Fisrst attempt when learn to code
        """
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                arr.pop()
                arr.insert(i+1, 0)
                i += 2
            else:
                i += 1