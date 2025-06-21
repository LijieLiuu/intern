# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root == None:
            return False
        if targetSum == None or targetSum == float("-inf"):
            return False

        dq = deque([(root, root.val)])

        while (len(dq)):
            node, curr_sum = dq.pop()
            if not node.left and not node.right and curr_sum == targetSum:
                return True

            if node.left:
                dq.append((node.left, curr_sum + node.left.val))
            if node.right:
                dq.append((node.right, curr_sum + node.right.val))
        return False