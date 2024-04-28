from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        believes = [0 for _ in range(n)]
        _believes = [0 for _ in range(n)]
        for item in trust:
            a, b = item
            believes[a - 1] += 1
            _believes[b - 1] += 1
        for i in range(n):
            if believes[i] == 0 and _believes[i] == n - 1:
                return i + 1
        return -1
    

if __name__ == '__main__':
    print(Solution().findJudge(2, [[1, 2]]))
    print(Solution().findJudge(3, [[1, 3], [2, 3]]))
    print(Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]))