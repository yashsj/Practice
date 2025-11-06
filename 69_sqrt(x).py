class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        ans=0
        while l<=r:
            middle=(l+(r-l)//2)
            if middle*middle>x:
                r=middle-1
            elif middle*middle<=x:
                l=middle+1
                ans=middle
            else:
                ans=middle
        return ans
