from collections import deque

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if edges is None:
            return 0

        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visited = {}
        count = 0
        dq = deque()

        for i in range(n):
            if i not in visited:
                count += 1
                visited[i] = True
                dq.append(i)
                while dq:
                    u = dq.pop()
                    for neighbor in adj[u]:
                        if neighbor not in visited:
                            visited[neighbor] = True
                            dq.append(neighbor)

        return count
