# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # # Brute Force
        # # Time:     O(n^2)
        # # Space:    O(n)
        # def maxH(root):
        #     if not root:
        #         return 0
        #     left = maxH(root.left)
        #     right = maxH(root.right)
        #     return 1 + max(left,right)

        # def dfs(root):
        #     if not root:
        #         return 0

        #     leftH = maxH(root.left)
        #     rightH = maxH(root.right)
        #     diameter = leftH+rightH
        #     subarray = max(dfs(root.left), dfs(root.right))
        #     return max(diameter,subarray)
        # return dfs(root)

        # # DFS
        # # Time:     O(n)
        # # Space:    O(h)// balanced tree: O(log(n)) // degenerate tree: O(n)
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return res
