class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p=len(nums)-1
        if(nums[0]==0 and len(nums)==1):
            pass
        else:
            for i in range(p-1,-1,-1):
                
                if(nums[i]==0):
                    for j in range(i,p,1):
                        nums[j]=nums[j+1]
                    nums[p]=0
                    p-=1
                #print(nums)