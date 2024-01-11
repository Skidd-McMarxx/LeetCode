from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        graph = defaultdict(list)

        def graph_mapper(node:TreeNode):
            if node.left:
                graph[node.left.val].append(node.val)
                graph[node.val].append(node.left.val)
                graph_mapper(node.left)
            if node.right:
                graph[node.right.val].append(node.val)
                graph[node.val].append(node.right.val)
                graph_mapper(node.right)

        graph_mapper(root)
        visited = set([start])
        going_to = deque([start])
        distance = 0
        while going_to:
            for _ in range(len(going_to)):
                node = going_to.popleft()
                for place in graph[node]:
                    if place not in visited:
                        visited.add(place)
                        going_to.append(place)
            if going_to:
                distance += 1

        return distance