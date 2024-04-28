from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     if root is None:
    #         return False
    #     if root.left is None and root.right is None:
    #         return root.val == targetSum
    #     return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        from collections import deque

        if not root:
            return False
        queue = deque([root])
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.left is None and node.right is None and node.val == targetSum:
                    return True
                if node.left:
                    queue.append(TreeNode(node.val + node.left.val, node.left.left, node.left.right))
                if node.right:
                    queue.append(TreeNode(node.val + node.right.val, node.right.left, node.right.right))
        return False