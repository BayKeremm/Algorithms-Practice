class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        indexUp = n
        indexDown=0
        while indexDown < indexUp:
            middle = indexDown + (indexUp - indexDown) / 2
            if isBadVersion(middle):
                indexUp = middle
            else:
                indexDown = middle + 1
        return indexDown