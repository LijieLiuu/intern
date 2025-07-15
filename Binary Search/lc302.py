class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:

        if image == None:
            return 0

        m, n = len(image), len(image[0])

        def blocks_row(row):
            for col in range(n):
                if image[row][col] == "1":
                    return True
            return False

        def blocks_col(col):
            for row in range(m):
                if image[row][col] == "1":
                    return True
            return False

        def get_min(left, right, check):
            while left < right:
                mid = (left + right) // 2
                if check(mid):
                    right = mid
                else:
                    left = mid + 1
            return left

        def get_max(left, right, check):
            while left < right:
                mid = math.ceil((left + right) / 2)
                if check(mid):
                    left = mid
                else:
                    right = mid - 1
            return left

        top = get_min(0, x, blocks_row)
        bottom = get_max(x, m - 1, blocks_row)
        left = get_min(0, y, blocks_col)
        right = get_max(y, n - 1, blocks_col)

        height = bottom - top + 1
        width = right - left + 1
        return height * width

