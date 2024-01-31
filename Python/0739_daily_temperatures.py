class Solution:
    """
    New List output
    """
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        answer = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                s_index, _ = stack.pop()
                answer[s_index] = index - s_index
            stack.append((index, temp))
        return answer


class Solution2:
    """
    Changes input list
    """
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                s_index, _ = stack.pop()
                temperatures[s_index] = index - s_index
            stack.append((index, temp))
            temperatures[index] = 0
        return temperatures
