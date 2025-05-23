class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hashmap=defaultdict(list)
        res=[]
        for s_id,score in items:
            hashmap[s_id].append(score)
        for student in hashmap:
            top5=sorted(hashmap[student],reverse=True)[:5]
            avg5=sum(top5)//5
            res.append([student,avg5])
        res.sort(key=lambda x:x[0])
        return res
