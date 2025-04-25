from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        level, index, queue = 1, 0, [[1]]
        while level <= k and index + 1 <= len(queue):
            start = index
            for _ in range(start, len(queue)):
                curr = queue[index]

                if len(curr) == k:
                    index += 1
                else:
                    del queue[0]
                    index = 0

                last = curr[-1]
                for next in range(last + 1, n + 1):
                    node = [*curr, next]
                    if len(node) > k:
                        node = node[1:]
                    queue.append(node)
            level += 1
        return queue


if __name__ == '__main__':
    for k in range(2, 4):
        print(f'C(6, {k})')
        print(Solution().combine(6, k))
        print('---')

                    
                
                
        
