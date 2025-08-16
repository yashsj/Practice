class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hashmap={}
        count=0
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1

        for num in hashmap:
            if num-k in hashmap:
                count+=hashmap[num]*hashmap[num-k]
        return count
        
        
