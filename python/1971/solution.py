from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import deque

        graph = [[0] * n for _ in range(n)]
        for edge in edges:
            u, v = edge
            graph[u - 1][v - 1], graph[v - 1][u - 1] = 1, 1
        
        queue = deque([source])
        

        