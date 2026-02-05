# class Solution:
#     def twosum(self,nums,target):
#         n=lens[nums]
#         for i in range(n):
#             for j in range(i+1,n):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]
#         return []
class Solution:
    def twoSum(self,nums,target):
        hashtable=dict()
        for i,num in enumerate(nums):
            if target-num in hashtable:
                return [hashtable[target-num],i]
            hashtable[num]=i
        return []

