from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        for i in range(rowIndex):
            result.append(1)
            for j in reversed(range(1, i + 1)):
                result[j] = result[j] + result[j - 1]
        return result


if __name__ == '__main__':
    for n in range(10):
        print(f"row {n}", Solution().getRow(n))