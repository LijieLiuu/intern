# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.flag_p = False
        self.flag_q = False

        def helper(node):
            if node == None:
                return None

            left = helper(node.left)
            right = helper(node.right)

            if node == p:
                self.flag_p = True
                return node
            if node == q:
                self.flag_q = True
                return node

            if left and right:
                return node

            return left or right

        ans = helper(root)
        return ans if self.flag_p == True and self.flag_q == True else None