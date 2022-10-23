import sys
from typing import List


class Solution:
    # Bad Solution On^2 time
    def maxSubArrayBad(self, nums: List[int]) -> int:
        largest_sum = -sys.maxsize - 1

        for i in range(len(nums)):
            curr_sum = 0

            for j in range(i, len(nums)):
                curr_sum = curr_sum + nums[j]
                if curr_sum > largest_sum:
                    largest_sum = curr_sum

        return largest_sum

    # Recursive solution  On^2 time
    def maxSubArrayRecurs(self, nums: List[int]) -> int:
        return self.helper(nums, 0, False)

    def helper(self,
               nums: List[int],
               i: int = 0,
               mustPick: bool = False) -> int:
        if i >= len(nums):
            if mustPick:
                return 0
            else:
                return -sys.maxsize - 1

        elif mustPick:
            return max(nums[i] + self.helper(nums, i + 1, True), 0)

        else:
            return max(self.helper(nums, i + 1, True),
                       nums[i] + self.helper(nums, i + 1, False))

        # Optimal Solution On time
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum = max(nums[i], nums[i] + cur_sum)
            max_sum = max(cur_sum, max_sum)

        return max_sum