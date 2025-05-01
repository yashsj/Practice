class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i,a in enumerate(nums):
            if a>0:
                break
            if a==nums[i-1] and i>0:
                continue
            left,right=i+1,len(nums)-1
            while left<right:
                threesum=nums[left]+nums[right]+nums[i]
                if threesum>0:
                    right-=1
                elif threesum<0:
                    left+=1
                else:
                    ans.append([nums[left],nums[right],nums[i]])
                    left+=1
                    right-=1
                    while nums[left]==nums[left-1] and left <right:
                        left+=1
        return ans
