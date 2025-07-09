class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == None or target == None:
            return -1
        pivot = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pivot = i + 1
                break

        if nums[pivot] <= target <= nums[-1]:
            left, right = pivot, len(nums)
        else:
            left, right = 0, pivot - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if left < len(nums) and nums[left] == target:
            return left
        return -1