from collections import deque

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        visited = {}
        for node in range(len(graph)):
            if node in visited:
                continue
            dq = deque([node])
            visited[node] = True

            while (len(dq)):
                top = dq.pop()
                for neighbour in graph[top]:
                    if neighbour not in visited and neighbour is not None:
                        dq.appendleft(neighbour)
                        visited[neighbour] = not visited[top]
                    else:
                        if visited[neighbour] == visited[top]:
                            return False
        return True



