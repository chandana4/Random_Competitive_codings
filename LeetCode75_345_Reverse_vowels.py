class Solution:
    def reverseVowels(self, s: str) -> str:
        str_len=s.count('')
        
        new_s=[]
        #vowels=['a','e','i','o','u','A','E','I','O','U']
        vowels='aeiouAEIOU'

        #print(str_len)
        str_len-=1
        j=str_len-1
        print(j)
        for i in range(0,str_len):
            new_s.append(s[i])
        i=0
        while(i<j):
            #print("Inside")
            if(new_s[i] in vowels):
                #print(new_s[i])
                if(new_s[j] in vowels):
                    temp=new_s[i]
                    print(temp)
                    new_s[i]=new_s[j]
                    new_s[j]=temp
                    i+=1
                    j-=1
                else:
                    j-=1
            else:
                i+=1
        s=''
        for i in range(0,str_len):
            s=s+new_s[i]
        return s
