from collections import defaultdict

class Solution:
    def pseudoPalindromicPaths (self, root:TreeNode) -> int:
        num_count = defaultdict(int)
        odd_tracker = 0

        def dfs(curr):
            nonlocal odd_tracker
            if not curr:
                return 0

            num_count[curr.val] += 1
            change = 1 if num_count[curr.val] % 2 == 1 else -1
            odd_tracker += change

            if not curr.left and not curr.right:
                res = 1 if odd_tracker <= 1 else 0
            else:
                res = dfs(curr.left) + dfs(curr.right)
            odd_tracker -= change
            num_count[curr.val] -= 1
            return res

        return dfs(root)
