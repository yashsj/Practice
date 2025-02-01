def fin(n):
    ans=0
    if n==1 or n==0:
        return n
    ans=fib(n-1)+fib(n-2)
    return ans 
    