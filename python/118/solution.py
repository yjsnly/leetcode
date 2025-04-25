from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = result[i - 1][j] + result[i - 1][j - 1]
            result.append(row)
        return result


if __name__ == '__main__':
    for n in range(1, 10):
        print(f"{n} rows", Solution().generate(n))
                