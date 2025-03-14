class TrieNode:
    def __init__(self):
        self.children={}
        self.isword=False
    
    def insert(self,word):
        cur=self
        for char in word:
            if char not in cur.children:
                cur.children[char]=TrieNode()
            cur=cur.children[char]
        cur.isword=True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for w in words:
            root.insert(w)
        ROWS,COLS=len(board),len(board[0])
        ans,visited=set(),set()
        def dfs(row,col,node,word):
            if row<0 or col<0 or row>=ROWS or col>=COLS or (row,col) in visited or board[row][col] not in node.children:
                return 
            

            visited.add((row,col))
            node=node.children[board[row][col]]
            word+=board[row][col]
            if node.isword:
                ans.add(word)
            dfs(row-1,col,node,word)
            dfs(row+1,col,node,word)
            dfs(row,col-1,node,word)
            dfs(row,col+1,node,word)
            
            visited.remove((row,col))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
        return list(ans)
        
