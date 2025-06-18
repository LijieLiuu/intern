# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        curr_level = [root]
        ans = []

        while (curr_level):
            values = []
            next_level = []

            for node in curr_level:
                values.append(node.val)
                if node.children:
                    next_level.extend(node.children)

            ans.append(values)
            curr_level = next_level
        return ans


