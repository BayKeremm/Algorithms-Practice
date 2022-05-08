class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        while left < right:
            middle = left + (right - left) / 2
            if nums[left] == target:
                return left
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        return left