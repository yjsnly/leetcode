class Solution:
    def climbStairs(self, n: int) -> int:
        # 动态规划
        # f(x) = f(x - 1) + f(x - 2)

        f1, f2 = 1, 1
        for _ in range(1, n):
           f1, f2 = f2, f1 + f2 
        return f2
    
        # TODO: 矩阵快速幂
        # TODO: 通项公式


if __name__ == '__main__':
    for n in range(10):
        print(Solution().climbStairs(n))