class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k > 0:
            n = len(nums)
            k = k % n
            nums[:] = nums[n-k:]+nums[:abs(k-n)]