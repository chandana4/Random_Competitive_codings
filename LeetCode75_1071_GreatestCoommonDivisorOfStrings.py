import string
class Solution(object):
    def gcdOfStrings(self, str1, str2):

        def valid(k):
            if len1%k or len2%k:
                return ""
            n1, n2 = len1//k, len2 //k #Floor division
            base = str1[:k]
            return str1==n1*base and str2 == n2*base



        len1, len2=len(str1), len(str2)
        for i in range(min(len1,len2),0,-1):
            if valid(i):
                return str1[:i]
        return ""

