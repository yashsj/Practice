class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[]
        total=0
        for num in nums:
            total+=num
            self.prefix.append(total)


    def sumRange(self, left: int, right: int) -> int:
        leftsum=self.prefix[left-1] if left>0 else 0
        rightsum=self.prefix[right]
        return (rightsum-leftsum)
        

