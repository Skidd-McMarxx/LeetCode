# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:

        def dfs(node:TreeNode, big, small):
            if not node:
                return big - small
            big = max(big, node.val)
            small = min(small, node.val)
            left_node = dfs(node.left, big, small)
            right_node = dfs(node.right, big, small)
            return max(left_node, right_node)


        return dfs(root, root.val, root.val) 