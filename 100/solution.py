from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if p is None and q is None:
    #         return True
    #     if p and q and p.val == q.val:
    #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #     return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            np, nq = stack.pop()
            if np is None and nq is None:
                continue
            if np is None or nq is None:
                return False
            if np.val != nq.val:
                return False
            else:
                stack.append((np.left, nq.left))
                stack.append((np.right, nq.right))
        return True



                

