from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        p, q = 0, 0
        while p < len(g) and q < len(s):
            if g[p] <= s[q]:
                p += 1
            q += 1
        return p

print(Solution().findContentChildren([1, 2, 3], [1, 1]))
print(Solution().findContentChildren([1, 2], [1, 2, 3]))
print(Solution().findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))

