class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        count={}
        for num in nums:
            count[num]=1+count.get(num,0)
        
        for val in count.values():
            if val >2:
                return False
        return True
        
