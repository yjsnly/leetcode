from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                result = max(result, prices[i] - min_price)
        return result

if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
    print(Solution().maxProfit([2, 4, 1]))
