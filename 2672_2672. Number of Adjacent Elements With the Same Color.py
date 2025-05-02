class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        res=[]
        ans=[0]*n
        count=0
        for index, color in queries:
            prev=ans[index-1] if index>0 else 0
            nxt=ans[index+1] if index<n-1 else 0
            if ans[index]==prev and ans[index]!=0:
                count-=1
            if ans[index]==nxt and ans[index]!=0:
                count-=1
            ans[index]=color

            if ans[index]==prev and ans[index]!=0:
                count+=1
            if ans[index]==nxt and ans[index]!=0:
                count+=1
            res.append(count)
        return res

            
