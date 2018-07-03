# 102. Binary Tree Level Order Traversal
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        if root == None:
            return result
        
        myq = []
        myq.insert(0, root)

        lq = []
        this_level = []
 
        while len(myq):
            front = myq.pop()
            this_level.append(front.val)
                        
            if front.left is not None:
                lq.insert(0, front.left)
            if front.right is not None:
                lq.insert(0, front.right)
    
            if len(myq) == 0:
                for node in (lq):
                    myq.append(node)    
                result.append(this_level)

                this_level = []
                lq = []
                
        return result