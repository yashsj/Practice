class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap={"2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"}
        res=[]
        def backtrack(i,curSet):
            if len(curSet)==len(digits):
                res.append(curSet)
                return 
            for char in hashmap[digits[i]]:
                backtrack(i+1,curSet+char)
        if digits:
            backtrack(0,"")
        return res



        
        
