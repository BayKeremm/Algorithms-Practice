class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        indexUp=len(nums)
        indexDown = 0
        
        for i in range(len(nums))
            indexMiddle = indexDown + (indexUp-indexDown) / 2
            
            if nums[indexMiddle] == target:
                return indexMiddle
            elif nums[indexMiddle] > target:
                indexUp = indexMiddle 
            else:
                indexDown = indexMiddle
            

        return -1