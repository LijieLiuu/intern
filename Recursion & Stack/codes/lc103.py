# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        curr_level = [root]
        ans = []

        index = 0
        while (curr_level):
            next_level = []
            values = []

            for node in curr_level:
                values.append(node.val)
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
            if index % 2 == 0:
                values.reverse()

            ans.append(values)
            curr_level = next_level
            index += 1
        return ans


