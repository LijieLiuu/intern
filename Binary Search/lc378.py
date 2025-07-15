class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0], matrix[n - 1][n - 1]

        def count(row, target):
            left, right = 0, len(row)

            while left < right:
                mid = (left + right) // 2
                if row[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return left

        while low < high:
            mid = (low + high) // 2
            cnt = 0
            for row in matrix:
                cnt += count(row, mid)

            if cnt >= k:
                high = mid
            else:
                low = mid + 1

        return low
