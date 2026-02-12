class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M=len(weight),capacity
        cache=[[-1]*(M+1) for _ in range(N)]
        return self.memoization(0,profit,weight,capacity,cache)

    def memoization(self,i,profit,weight,capacity,cache):
        if i==len(weight):
            return 0
        
        if cache[i][capacity]!=-1:
            return cache[i][capacity]
        cache[i][capacity]=self.memoization(i+1,profit,weight,capacity,cache)


        #Include the next item in the knapsack 
        newCap=capacity-weight[i]
        if newCap>=0:
            p=profit[i]+self.memoization(i+1,profit,weight,newCap,cache)
            cache[i][capacity]=max(p,cache[i][capacity])
        return cache[i][capacity]
