class Solution:
    def lengthOfLongestSubstring(self,s):
        n=len(s)
        right=-1
        ans=0
        occ=set()
        for i in range(n):
            if i!=0:
                occ.remove(s[i-1])
            while right+1<n and s[right+1]not in occ:
                occ.add(s[right+1])
                right+=1
            ans=max(ans,right-i+1)
        return ans