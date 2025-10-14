class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def freq(word):
            res=[0]*26
            for char in word:
                res[ord(char)-ord('a')]+=1
            return res

        firstWord=freq(words[0])
        result=[words[0]]
        for i in range(1,len(words)):
            curWord=freq(words[i])
            if curWord!=firstWord:
                result.append(words[i])
                firstWord=curWord
        return result        

#Time complexity: O(N*m(the number of words x avg length of the word ))
#space complexity: O(1) auxiliary (or O(n × m) if counting output)
