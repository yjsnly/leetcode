from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:

    #     def deepth(_root: Optional[TreeNode]) -> int:
    #         if not _root:
    #             return 0
    #         return 1 + max(deepth(_root.left), deepth(_root.right))
        
    #     if not root:
    #         return True
        
    #     delta = abs(deepth(root.left) - deepth(root.right))
    #     return delta < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(_root: Optional[TreeNode]) -> Tuple[int, bool]:
            if not _root:
                return 0, True
            deepth_left, balanced_left = dfs(_root.left)
            if not balanced_left:
                return -1, False
            deepth_right, balanced_right = dfs(_root.right)
            if not balanced_right:
                return -1, False
            if abs(deepth_left - deepth_right) > 1:
                return -1, False
            return 1 + max(deepth_left, deepth_right), True
                  
        if not root:
            return True     
        _, balanced = dfs(root)
        return balanced


        