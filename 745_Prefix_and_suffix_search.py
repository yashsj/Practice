class TrieNode:
    def __init__(self):
        self.children={}
        self.index=-1

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert_word(self,word,index):
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
            cur.index=index


    def starts_with(self,word):
        cur=self.root
        for c in word:
            if c not in cur.children:
                return -1
            cur=cur.children[c]
        return cur.index

            
class WordFilter:
    def __init__(self, words: List[str]):
        self.trie=Trie()
        for index,word in enumerate(words):
            word=word+"#"+word

            for i in range(len(word)):
                self.trie.insert_word(word[i:],index)




    def f(self, pref: str, suff: str) -> int:
        return self.trie.starts_with(suff+"#"+pref)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
