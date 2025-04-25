from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [values[j] - j for j in range(1, len(values))]
        for j in range(len(dp) - 1, 0, -1):
            if dp[j - 1] < dp[j]:
                dp[j - 1] = dp[j]
        return max(values[i] + i + dp[i] for i in range(len(values) - 1))


print(Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]))
print(Solution().maxScoreSightseeingPair([1, 2]))
print(Solution().maxScoreSightseeingPair([2, 2, 2]))