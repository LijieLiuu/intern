from collections import deque


class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if maze == None:
            return False
        if start == None:
            return False
        if destination == None:
            return False

        m, n = len(maze), len(maze[0])
        seen = [[False] * n for _ in range(m)]
        q = deque([tuple(start)])
        seen[start[0]][start[1]] = True

        while q:
            x, y = q.popleft()
            if [x, y] == destination:
                return True
            for dx, dy in ([1, 0], [-1, 0], [0, 1], [0, -1]):
                nx, ny = x, y
                while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                if not seen[nx][ny]:
                    seen[nx][ny] = True
                    q.append((nx, ny))
        return False

