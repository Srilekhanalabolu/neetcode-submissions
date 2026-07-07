class Solution:
    def twosum(self,nums,target,i,j,res):
        while(i<j):
            if(nums[i]+nums[j]>target):
                j-=1
            elif(nums[i]+nums[j]<target):
                i+=1
            else:
                res.append([-target, nums[i], nums[j]])
                while(i<j and nums[i]==nums[i+1]):
                    i+=1
                while(i<j and nums[j]==nums[j-1]):
                    j-=1
                i += 1
                j -= 1
      
                
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            n1=nums[i]
            target=-n1
            self.twosum(nums,target,i+1,n-1,res)
        return res

            
        