from collections import defaultdict, deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val: int = 0,
                 left: 'Optional[TreeNode]' = None,
                 right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        cols = defaultdict(list)
        q = deque([(root, 0)])
        min_c = max_c = 0

        while q:
            node, c = q.popleft()
            cols[c].append(node.val)
            min_c = min(min_c, c)
            max_c = max(max_c, c)

            if node.left:
                q.append((node.left, c - 1))
            if node.right:
                q.append((node.right, c + 1))

        # 按列号从小到大输出
        return [cols[c] for c in range(min_c, max_c + 1)]