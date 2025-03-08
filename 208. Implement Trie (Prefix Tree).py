class TreeNode:
    def __init__(self):
        self.eow=False
        self.child={}
class Trie:

    def __init__(self):
        self.root=TreeNode()

    def insert(self, word: str) -> None:
        curr=self.root
        for char in word:
            if char not in curr.child:
                curr.child[char]=TreeNode()
            curr=curr.child[char]
        curr.eow=True


    def search(self, word: str) -> bool:
        curr=self.root
        for char in word:
            if char not in curr.child:
                return False
            curr=curr.child[char]
        return  curr.eow
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for char in prefix:
            if char not in curr.child:
                return False
            curr=curr.child[char]
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
