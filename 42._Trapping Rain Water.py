class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxLeft,maxRight=height[0],height[right]
        res=0
        while left<right: 
            if height[left]<height[right]:
                
                maxLeft=max(height[left],maxLeft)
                res+=(maxLeft-height[left])
                left+=1
            else:
                
                maxRight=max(height[right],maxRight)
                res+=maxRight-height[right]
                right-=1
        return res
