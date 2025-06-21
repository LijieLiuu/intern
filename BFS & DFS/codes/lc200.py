from collections import deque


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    grid[i][j] = "0"

                    queue = deque([(i, j)])

                    while (queue):
                        x, y = queue.popleft()
                        for dx, dy in ([0, -1], [0, 1], [-1, 0], [1, 0]):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                                grid[nx][ny] = "0"
                                queue.append((nx, ny))
        return count


