class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans=[[] for _ in range(len(people))]
        people.sort(key=lambda x:(x[0],-x[1]))
        for p in people:
            cnt=i=0
            while i<len(people):
                if not ans[i]:
                    if cnt==p[1]:
                        break
                    cnt+=1
                i+=1
            ans[i]=p
        return ans






        
