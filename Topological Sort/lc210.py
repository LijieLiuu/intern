from collections import deque


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses == None or prerequisites == None:
            return []

        indegree = [0] * numCourses
        for a, b in prerequisites:
            indegree[a] += 1

        dq = deque([i for i in range(numCourses) if indegree[i] == 0])
        ans = []
        while len(dq):
            top = dq.pop()
            ans.append(top)

            for courses in prerequisites:
                if courses[1] == top:
                    indegree[courses[0]] -= 1

                if indegree[courses[0]] == 0:
                    dq.appendleft(courses[0])

        if len(ans) != numCourses:
            return []
        return ans

if __name__ == "__main__":
    tests = [
        (2, [[1, 0]]),                       # Example 1
        (4, [[1,0], [2,0], [3,1], [3,2]]),   # Example 2
        (1, []),                             # Example 3: single course
        (2, [[0,1], [1,0]]),                 # Cycle -> []
        (3, [[1,0], [2,1]]),                 # Linear chain [0,1,2]
    ]

    solution = Solution()
    for idx, (n, prereq) in enumerate(tests, 1):
        order = solution.findOrder(n, prereq)
        print(f"Test case {idx}: numCourses = {n}, prerequisites = {prereq}")
        print(f" -> Course order: {order}\n")