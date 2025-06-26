# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def helper(root):
            if root == None:
                return 0
            if root.left == None and root.right == None:
                return 1
            elif root.left != None and root.right == None:
                return 1 + helper(root.left)
            elif root.left == None and root.right != None:
                return 1 + helper(root.right)
            else:
                return 1 + min(helper(root.left), helper(root.right))

        return helper(root)

