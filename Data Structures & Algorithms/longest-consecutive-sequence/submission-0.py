class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=0
        for num in nums:
            if num-1 not in nums:
                curr=num
                cnt=1
                while curr+1 in nums:
                    curr+=1
                    cnt+=1
                ans=max(ans,cnt)
        return ans
                