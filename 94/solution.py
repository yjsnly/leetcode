from typing import List, Optional

import ipdb


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     ans = []

    #     def dfs(_root: Optional[TreeNode]):
    #         if not _root:
    #             return
    #         dfs(_root.left)
    #         ans.append(_root.val)
    #         dfs(_root.right)
        
    #     dfs(root)

    #     return ans

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, stack = [], []
        if not root:
            return ans

        p: Optional[TreeNode] = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            ans.append(p.val)
            p = p.right
        return ans


    

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().inorderTraversal(root))