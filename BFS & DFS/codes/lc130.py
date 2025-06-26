class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board == None:
            return

        dq = deque()

        for i in range(len(board)):
            for j in (0, len(board[0]) - 1):
                if board[i][j] == 'O':
                    dq.append((i, j))
                    board[i][j] = '#'

        for j in range(len(board[0])):
            for i in (0, len(board) - 1):
                if board[i][j] == 'O':
                    dq.append((i, j))
                    board[i][j] = '#'

        while dq:
            x, y = dq.pop()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 'O':
                    board[nx][ny] = '#'
                    dq.append((nx, ny))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'