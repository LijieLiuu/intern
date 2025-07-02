# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def helper(node):
            if node == None:
                return 0, None

            left, l_lca = helper(node.left)
            right, r_lca = helper(node.right)

            if left > right:
                return left + 1, l_lca
            if right > left:
                return right + 1, r_lca
            else:
                return left + 1, node

        return helper(root)[1]