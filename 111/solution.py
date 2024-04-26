from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        if not root:
            return 0
        ans, queue = 1, deque([root])
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.left is None and node.right is None:
                    return ans
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans += 1
        return ans
