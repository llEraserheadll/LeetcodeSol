# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        n = len(preorder)
        
        root = preorder[0]
        node = TreeNode(root)
        pos = inorder.index(root)
        inorder_left, inorder_right = inorder[:pos], inorder[pos+1:]
        
        left_tree = self.buildTree(preorder[1:1+len(inorder_left)], inorder_left) 
        right_tree = self.buildTree(preorder[1+len(inorder_left):], inorder_right) 
        node.left, node.right = left_tree, right_tree
        
        return node

        