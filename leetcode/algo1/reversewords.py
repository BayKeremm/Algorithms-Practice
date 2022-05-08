class Solution:
    def reverseWords(self, s: str) -> str:
        
        res = ""
        data = s.split()
        for i in data:
            res= res + i[::-1] + " "
        return res.rstrip()
  