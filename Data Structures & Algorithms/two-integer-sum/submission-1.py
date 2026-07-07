class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1={}
        for index,value in enumerate(nums):
            ans=target-value
            if ans in map1:
                return [map1[ans],index]
            map1[value]=index
            