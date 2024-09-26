class Solution:
    def traverse(self, node, final, temp):
        if not node:
            return None

        temp.append(str(node.val))

        if not node.left and not node.right:
            final.append("->".join(temp))

        self.traverse(node.left, final, temp)
        self.traverse(node.right, final, temp)
        temp.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        final = []
        temp = []
        self.traverse(root, final, temp)
        return final
