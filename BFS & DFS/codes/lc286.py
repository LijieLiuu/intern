from collections import deque


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if rooms == None:
            return None

        INF = 2**31 - 1
        gates = []
        dq = deque()
        visited = {}
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    dq.append((i, j))
                    visited[(i, j)] = 0

        while dq:
            x, y = dq.pop()
            cur_dist = visited[(x, y)]
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < len(rooms) and 0 <= ny < len(rooms[0]) and rooms[nx][ny] == INF and (nx, ny) not in visited:
                    visited[(nx, ny)] = cur_dist +1
                    dq.appendleft((nx, ny))

            for (i, j), dist in visited.items():
                rooms[i][j] = dist
        return

