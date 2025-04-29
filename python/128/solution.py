from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        result = 0
        for x in nums:
            if x - 1 in set_nums:
                continue
            
            curr, length = x, 1
            while curr + 1 in set_nums:
                curr, length = curr + 1, length + 1
            result = max(result, length)
            
        return result
    
print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(Solution().longestConsecutive([1, 0 ,1, 2]))