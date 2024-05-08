class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_a=0
        while(left<right):
            curr_a=min(height[left],height[right])*(right-left)
            if(max_a<curr_a):
                max_a=curr_a
            if(height[left]< height[right]):
                left+=1
            else:
                right-=1
        return max_a