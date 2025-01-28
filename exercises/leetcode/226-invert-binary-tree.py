# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # # Recursive DFS
        # # Time complexity: O(n) 
        # # Space complexity: O(n)
        # def dfs(root):
        #     if not root:
        #         return

        #     root.left, root.right =  root.right, root.left
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # return root 

        # # TODO: Breadth First Search
        # # Time complexity: O(n) 
        # # Space complexity: O(n)
        # def bfs(root):
        #     if not root:
        #         return
        #     q = deque([root])
        #     while q:
        #         node = q.popleft()
        #         node.left, node.right =  node.right, node.left
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # bfs(root)
        # return root

        # TODO: Iterative DFS
        # Time complexity: O(n) 
        # Space complexity: O(n)
        def interativeDFS(root):
            if not root:
                return
            stack = [root]
            while stack:
                node = stack.pop()
                node.left, node.right =  node.right, node.left
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        interativeDFS(root)
        return root

        
