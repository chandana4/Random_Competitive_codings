class Solution(object):
    def findMaxAverage(self, nums, k):
        maxsum=sum(nums[:k])
        sum_c=maxsum
        left=0
        right=k
        while(right<=len(nums)-1):
            sum_c=sum_c-nums[left]+nums[right]
            left+=1
            right+=1
            if(sum_c>maxsum):
                maxsum=sum_c
        return maxsum/float(k)