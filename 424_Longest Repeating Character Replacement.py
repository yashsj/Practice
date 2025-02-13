class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        res=0
        ans=0
        hashmap={}
        for right in range(len(s)):
            hashmap[s[right]]=1+hashmap.get(s[right],0)
            ans=max(ans,hashmap[s[right]])

            while (right-left+1)-ans>k:
                hashmap[s[left]]-=1
                left+=1
            res=max(res,right-left+1)
        return res
