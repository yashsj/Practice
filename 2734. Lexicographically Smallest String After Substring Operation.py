class Solution:
    def smallestString(self, s: str) -> str:
        count=0
        arr=[char for char in s]
        for i in range(len(s)):
            if arr[i]>'a':
                arr[i]=chr(ord(arr[i])-1) #change to the prev char
                count+=1
            elif count>0:
                break
        if count==0:
            arr[len(s)-1]='z'
        return  "".join(arr)
