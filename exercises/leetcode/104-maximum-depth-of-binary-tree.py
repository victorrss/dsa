# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # Recursive DFS
        # # Time:     O(n)
        # # Space:    O(n)
        # def dfs(root):
        #     if not root:
        #         return 0
        #     return 1 + max(dfs(root.left), dfs(root.right))
        # return dfs(root)

        # # BFS
        # # Time:     O(n)
        # # Space:    O(n)
        # def bfs(root):
        #     q = deque()
        #     if root:
        #         q.append(root)
        #     res = 0
        #     while q:
        #         for i in range(len(q)): # to run for each level
        #             node = q.popleft()
        #             if node.left:
        #                 q.append(node.left)
        #             if node.right:
        #                 q.append(node.right)
        #         res+=1
        #     return res
        # return bfs(root)

        # Interative DFS
        # Time:     O(n)
        # Space:    O(n)
        def intDFS(root):
            stack = [[root, 1]]
            res = 0
            while stack:
                node, level = stack.pop()
                if not node:
                    continue

                res = max(res, level)

                stack.append([node.left, level + 1])
                stack.append([node.right, level + 1])
            return res

        return intDFS(root)
