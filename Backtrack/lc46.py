class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == None:
            return []

        ans = []

        def backtrack(path, length):
            if len(path) == length:
                ans.append(path[:])
                return
            for i in range(0, length):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(path, length)
                path.pop()

        backtrack([], len(nums))
        return ans