class Solution(object):
    def mergeAlternately(self, word1, word2):
        odd_or_even=1
        merged=[]
        c1=0
        c2=0
        for i in range(0,(len(word1)+len(word2))):
            if(odd_or_even%2==1):
                if(c1<len(word1)):
                    merged.append(word1[c1])
                    c1+=1
                else:
                    while(c2<len(word2)):
                        merged.append(word2[c2])
                        c2+=1
            else:
                if(c2<len(word2)):
                    merged.append(word2[c2])
                    c2+=1
                else:
                    while(c1<len(word1)):
                        merged.append(word1[c1])
                        c1+=1
            odd_or_even+=1
        return(''.join(merged))
