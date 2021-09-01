"""Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

 

Constraints:

    n == nums.length
    1 <= n <= 104
    -105 <= nums[i] <= 105

"""

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        total = len(nums)
        if total < 3:
            return True
        local_min = 0
        checkpoint = None
        A = nums[0]
        B = nums[1]
        min_started = None
        for ind in range(0, total - 1):
            A = nums[ind]
            B = nums[ind + 1]

            if A > B:
                local_min += 1
                min_started = A
                if ind > 0:
                    checkpoint = ind - 1
            else:
                if min_started is not None:
                    if B < min_started:
                        if checkpoint is not None:
                            if B >= nums[checkpoint] and A >= nums[checkpoint]:
                                min_started = None
                            else:
                                return False
                    else:
                        min_started = None

            if local_min > 1:
                return False

        return True


sol = Solution()
print(sol.checkPossibility([1, 4, 1, 2]))
