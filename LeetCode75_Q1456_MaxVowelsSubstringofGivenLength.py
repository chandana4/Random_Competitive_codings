class Solution(object):
    def maxVowels(self, s, k):
        n=len(s)
        i=0
        n_vow=[0]*n
        vowels='aeiouAEIOU'
        while(i<n):
            if(s[i] in vowels):
                n_vow[i]=1
            else:
                n_vow[i]=0
            i+=1
        max_sum=sum(n_vow[0:k])
        print(n_vow,max_sum)
        cur_sum=max_sum
        left=0
        right=k
        while(right<n):
            cur_sum=cur_sum+n_vow[right]-n_vow[left]
            print(cur_sum)
            right+=1
            left+=1
            if(cur_sum>max_sum):
                max_sum=cur_sum
        return max_sum