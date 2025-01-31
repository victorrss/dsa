# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxH(root):
            if not root:
                return 0
            return 1 + max(maxH(root.left), maxH(root.right))

        if not root:
            return True

        left = maxH(root.left)
        right = maxH(root.right)
        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
