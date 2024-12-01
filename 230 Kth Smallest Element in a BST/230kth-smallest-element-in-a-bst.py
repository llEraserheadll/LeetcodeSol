# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        count = 0

        while stack or current:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Visit the node
            current = stack.pop()
            count += 1

            # If we have visited k nodes, return the current node's value
            if count == k:
                return current.val

            # Move to the right subtree
            current = current.right