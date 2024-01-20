class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 1_000_000_007
        result = 0
        stack = []
        for index, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                stack_index = stack.pop()
                next_stack_index = stack[-1] if stack else -1
                result = (result + arr[stack_index] * (index - stack_index) *
                          (stack_index - next_stack_index)) % MOD
            stack.append(index)

        while stack:
            stack_index = stack.pop()
            next_stack_index = stack[-1] if stack else -1
            result = (result + arr[stack_index] * (len(arr) - stack_index) *
                      (stack_index - next_stack_index)) % MOD

        return result
