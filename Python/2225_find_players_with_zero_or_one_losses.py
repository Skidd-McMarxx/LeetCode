from collections import defaultdict

class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        lose_count = defaultdict(int)
        for win, lose in matches:
            lose_count[win] += 0
            lose_count[lose] += 1

        winners, second = [], []
        for key in lose_count:
            if lose_count[key] == 0:
                winners.append(key)
            elif lose_count[key] == 1:
                second.append(key)
        return [sorted(winners), sorted(second)]