class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res=0
        for i in range(len(s)-2):
            substring=s[i:i+3]
            if substring[0]==substring[1] or substring[0]==substring[2] or substring[1]==substring[2]:
                continue 
            res+=1
        return res
