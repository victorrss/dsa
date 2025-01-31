# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
       
        if not p or not q:
            return False
    
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # # DFS
        # # Time: O(n)
        # # Space: O(n) // Best: O(log(n)) // Worst: O(n)
        # if not p and not q:
        #     return True

        # if p and q and p.val == q.val:
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # else:
        #     return False
        
        # # Interative DFS
        # # Time: O(n)
        # # Space: O(n)
        # stack = [(p,q)]

        # while stack:
        #     P,Q = stack.pop()

        #     if not P and not Q:
        #         continue
        #     elif not P or not Q or P.val != Q.val:
        #         return False
        #     else:
        #         stack.append((P.left,Q.left))
        #         stack.append((P.right,Q.right))
        # return True

        # # BFS
        # # Time: O(n)
        # # Space: O(n)
        # if not p and not q:
        #     return True

        # queue = deque([(p,q)])

        # while queue: 
        #     P,Q = queue.popleft()

        #     if not P and not Q:
        #         continue
        #     elif not P or not Q or P.val != Q.val:
        #         return False
        #     else:
        #         queue.append((P.left,Q.left))
        #         queue.append((P.right,Q.right))
        # return True
