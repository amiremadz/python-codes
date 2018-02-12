# 98. Validate Binary Search Tree
# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inf = float("Inf")
        return self.helper(root, -inf, inf)
    
    def helper(self, root, minval, maxval):
        if root == None:
            return True
        
        if (root.val <= minval) or (root.val >= maxval):
            return False
        
        left  = self.helper(root.left, minval, root.val)
        right = self.helper(root.right, root.val, maxval)
        
        return left and right