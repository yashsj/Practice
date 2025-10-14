class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res=list(s)
        for i in range(0,len(s),2*k):
            res[i:i+k]=reversed(res[i:i+k])
        return "".join(res)
