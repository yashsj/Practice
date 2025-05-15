class Solution:
    def isPalindrome(self, x: int) -> bool:
        org,reversed_num=x,0
        if org<0:
            return False
        while x>0:
            reversed_num=reversed_num*10+x%10
            x=x//10
        return reversed_num==org

