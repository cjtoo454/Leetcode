class Solution:
    def maxSubArray(self,nums):
        pre_max=0
        max_sum=nums[0]
        for num in nums:
            pre_max=max(pre_max+num,num)
            max_sum=max(max_sum,pre_max)
        return max_sum