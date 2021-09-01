"""
653. Two Sum IV - Input is a BST
Easy

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Example 3:

Input: root = [2,1,3], k = 4
Output: true

Example 4:

Input: root = [2,1,3], k = 1
Output: false

Example 5:

Input: root = [2,1,3], k = 3
Output: true

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -104 <= Node.val <= 104
    root is guaranteed to be a valid binary search tree.
    -105 <= k <= 105

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        print(root)
        if root.val == k:
            return True
        search_val = k - root.val
        if search_val < root.val:
            if root.left is not None:
                if self.findTarget(root.left, search_val):
                    return True
        if search_val > root.val:
            if root.right is not None:
                if self.findTarget(root.right, search_val):
                    return True

        return False


sol = Solution()
node=TreeNode([5, 3, 6, 2, 4, None, 7])
print(sol.findTarget(root=, k=28))
