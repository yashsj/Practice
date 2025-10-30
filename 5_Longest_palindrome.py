class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resLen=0
        #if we have an odd length
        for i in range(len(s)):
            left,right=i,i
            while left>=0 and right<len(s) and s[left]==s[right]:
                if (right-left+1)>resLen:
                    resLen=right-left+1
                    res=s[left:right+1]
                left-=1
                right+=1

        #if we had an even length-array
        for i in range(len(s)):
            left,right=i,i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                if (right-left+1)>resLen:
                    resLen=right-left+1
                    res=s[left:r+1]
                left-=1
                right+=1
        return res

        
        
