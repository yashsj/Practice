class Solution:
    def numberOfSteps(self, num: int) -> int:
        opr=0
        while num:
            if num%2==0:
                num=num/2
                opr+=1
            else:
                num-=1
                opr+=1
        return opr
