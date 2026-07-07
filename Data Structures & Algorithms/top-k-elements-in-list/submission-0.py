class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_freq={}
        for num in nums:
            cnt_freq[num]=cnt_freq.get(num,0)+1
        sorted_items=sorted(cnt_freq.items(),key=lambda x:x[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(sorted_items[i][0])
        return res
        