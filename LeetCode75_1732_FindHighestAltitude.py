class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        g,maxi=0,0
        for i in gain:
            g=g+i
            if(g>maxi):
                maxi=g
        return maxi
