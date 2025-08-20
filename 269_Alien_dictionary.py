class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj={c:set() for word in words for c in word} 
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            minLen=min(len(w1),len(w2))
            if w1>w2 and w1[:minLen]==w2[:minLen]:
                return ""
            for j in range(minLen):
               if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
            
        visited=set()
        path=set()
        res=[]

        def dfs(char):
            if char in path:
                return False
            if char in visited:
                return True
            path.add(char)
            for neigh in adj[char]:
                if not dfs(neigh):
                    return False
            path.remove(char)
            visited.add(char)
            res.append(char)
            return True
        
        for char in adj:
            if not dfs(char):
                return ""
        return "".join(res[::-1])

        
