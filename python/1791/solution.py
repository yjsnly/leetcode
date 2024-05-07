from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [0] * n
        for item in edges:
            u, v = item
            graph[u - 1] += 1
            graph[v - 1] += 1
        for i in range(n):
            if graph[i] == n - 1:
                return i + 1
        return -1


if __name__ == '__main__':
    print(Solution().findCenter([[1, 2], [2, 3], [4, 2]]))
    print(Solution().findCenter([[1, 2],[5, 1],[1, 3],[1, 4]]))
