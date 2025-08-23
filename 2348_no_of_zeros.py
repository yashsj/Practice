class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count=0
        tot=0
        for num in nums:
            if num==0:
                count+=1
            else:
                count=0
            tot+=count
        return tot
        
