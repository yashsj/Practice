class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        longer=0
        for n in hashset:
            if (n-1) not in hashset:
                cur_len=1
                while (n+cur_len) in hashset:
                    cur_len+=1
                longer=max(longer,cur_len)
        return longer


    
  
