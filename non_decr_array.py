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
        local_max = 0
        ind = len(nums) - 1
        if ind < 3:
            return True

        while ind > 1:
            A = nums[ind - 2]
            B = nums[ind - 1]
            C = nums[ind]
            print(f'{A=} {B=} {C=} {local_max=} {ind=}')
            if local_max == 2:
                return False
            if A > B and B > C:
                return False
            if B > C:
                local_max += 1
            if A > C:
                local_max += 1
            ind -= 1

        return True


sol = Solution()
print(sol.checkPossibility([3, 4, 2, 3]))
