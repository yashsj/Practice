class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        hashmap={}
        for num in nums:
            hashmap[num]=hashmap.get(num,0)+1
            if hashmap[num]==2:
                res.append(num)
        return res
            
        
