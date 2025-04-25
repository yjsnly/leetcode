from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        from collections import deque
        table = [
            '', 'abc', 'def',
            'ghi', 'jkl', 'mno',
            'pqrs', 'tuv', 'wxyz'
        ]
        if len(digits) == 0:
            return []
        result = deque([''])
        for digit in digits:
            n = len(result)
            for _ in range(n):
                prev = result.popleft()
                for ch in table[ord(digit) - 49]:
                    result.append(f'{prev}{ch}')
        return list(result)


print(Solution().letterCombinations('23'))
print(Solution().letterCombinations(''))
print(Solution().letterCombinations('2'))