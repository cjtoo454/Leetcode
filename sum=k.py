class Solution:
    def subarraySum(self,nums,k):
        sum_book=dict
        sum_book={0,1}
        ans=0
        current_sum=0
        for num in nums:
            current_sum+=num
            target=current_sum-k
            if target in sum_book:
                ans+=sum_book[target]
            sum_book[current_sum]=sun_book.get(current_sum,0)+1
        return ans