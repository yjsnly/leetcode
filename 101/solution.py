from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:

    #     def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #         if p is None and q is None:
    #             return True
    #         if p is None or q is None:
    #             return False
    #         if p.val != q.val:
    #             return False
    #         else:
    #             return dfs(p.left, q.right) and dfs(p.right, q.left)
        
    #     if root is None:
    #         return True
    #     return dfs(root.left, root.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            p, q = stack.pop()
            if p is None and q is None:
                continue
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            stack.append((p.left, q.right))
            stack.append((p.right, q.left))
        return True
