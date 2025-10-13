class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            new_list=list()
            for i in range(len(nums)-1):
                new_list.append((nums[i]+nums[i+1])%10)
            nums=new_list
        return nums[0]
