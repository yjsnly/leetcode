from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans, stack = [], []
        def dfs(i: int, _sum: int):
            if len(stack) == k and _sum == n:
                ans.append(stack.copy())
            elif len(stack) < k and _sum + i < n:
                for j in range(i, 10):
                    stack.append(j)
                    dfs(j + 1, _sum + j)
                    stack.pop()
        dfs(1, 0)
        return ans


if __name__ == '__main__':
    print(Solution().combinationSum3(3, 7))