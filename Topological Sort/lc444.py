from collections import deque


class Solution(object):
    def sequenceReconstruction(self, nums, sequences):
        """
        :type nums: List[int]
        :type sequences: List[List[int]]
        :rtype: bool
        """
        if nums == None and sequences == None:
            return False

        edges = []
        for seq in sequences:
            for i in range(len(seq) - 1):
                edges.append((seq[i] - 1, seq[i + 1] - 1))

        nexts = {i: [] for i in range(len(nums))}
        indegree = [0] * len(nums)
        for a, b in edges:
            nexts[a].append(b)
            indegree[b] += 1

        dq = deque([i for i in range(len(nums)) if indegree[i] == 0])
        ans = []
        while dq:
            if len(dq) > 1:
                return False
            top = dq.pop()
            ans.append(top)

            for temp in nexts[top]:
                indegree[temp] -= 1
                if indegree[temp] == 0:
                    dq.appendleft(temp)

        for i in range(len(ans)):
            ans[i] += 1
        if ans == nums:
            return True
        return False
