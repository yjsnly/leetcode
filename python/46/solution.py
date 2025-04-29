from typing import List
from itertools import chain

class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums) == 1:
    #         return [[nums[0]]]
    #     if len(nums) == 2:
    #         return [[nums[0], nums[1]], [nums[1], nums[0]]]
    #     if len(nums) == 3:
    #         return [
    #             [nums[0], nums[1], nums[2]],
    #             [nums[0], nums[2], nums[1]],
    #             [nums[1], nums[0], nums[2]],
    #             [nums[1], nums[2], nums[0]],
    #             [nums[2], nums[0], nums[1]],
    #             [nums[2], nums[1], nums[0]]
    #         ]     
    #     return list(chain.from_iterable([
    #         [
    #             [x, *item]
    #             for item in self.permute([y for y in nums if x != y])
    #         ]
    #         for x in nums
    #     ]))

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        if len(nums) == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        if len(nums) == 3:
            return [
                [nums[0], nums[1], nums[2]],
                [nums[0], nums[2], nums[1]],
                [nums[1], nums[0], nums[2]],
                [nums[1], nums[2], nums[0]],
                [nums[2], nums[0], nums[1]],
                [nums[2], nums[1], nums[0]]
            ] 
        stack, result = [(nums, [])], []
        while stack:
            remain, current = stack.pop()
            if not remain:
                result.append(current)
            else:
                for i in range(len(remain)):
                    stack.append(([*remain[:i], *remain[i+1:]], [*current, remain[i]]))
        return result


print(Solution().permute([1, 2, 3, 4]))