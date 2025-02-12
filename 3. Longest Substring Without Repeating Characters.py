class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        left=0
        hashset=set()
        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left+=1
            hashset.add(s[right])
            ans=max(ans,right-left+1)
        return ans
