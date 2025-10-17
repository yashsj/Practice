class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
       
        n,m=len(s),len(t)
        count=0
        i,j=0,0
        if abs(m-n)>1:
            return False
        while i<n and j<m:
            if s[i]!=t[j]:
                if count==1:
                    return False
                if n>m:
                    i+=1
                elif m>n:
                    j+=1
                else:
                    i+=1
                    j+=1
                count+=1
            
            else:
                i+=1
                j+=1
        if i<n or j<m:
            count+=1
        return count==1

        
