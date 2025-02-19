class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quad(n):
            return a*n*n+b*n+c
        n=len(nums)
        left,right,res=0,n-1,[0]*(n)
        index=0 if a<0 else n-1
        while left<=right:
            left_res,right_res=quad(nums[left]),quad(nums[right])
            if a>=0:
                if left_res>right_res:
                    res[index]=left_res
                    left+=1
                else:
                    res[index]=right_res
                    right-=1
                index-=1
            else:
                if left_res>right_res:
                    res[index]=right_res
                    right-=1
                else:
                    res[index]=left_res
                    left+=1
                index+=1
        return res


        
