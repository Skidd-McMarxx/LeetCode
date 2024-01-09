class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:    
    def leafSimilar(self, root1:TreeNode, root2:TreeNode) -> bool:
        def deep_search(root, leaf:list):    
            if not root:
                return
            if not root.left and not root.right:
                leaf.append(root.val)
                return 
            deep_search(root.left, leaf)
            deep_search(root.right, leaf)

        leaf1, leaf2 = [], []
        deep_search(root1, leaf1)
        deep_search(root2, leaf2)
        return leaf1 == leaf2