class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        left=right=0
        
        while(right<n):
            if(nums[right]==0):
                k-=1
            
            if k<0:
                if nums[left]==0:
                    k+=1
                left+=1
            right+=1




        return right-left

