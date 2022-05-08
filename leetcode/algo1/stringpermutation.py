class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        n = len(s2)
        s = sorted(s1)
        for i in range(0,n):
            if i+window <=n and s == sorted(s2[i:i+window]):
                return True
        return False
        