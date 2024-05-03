class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        new_str=[]
        for word in s:
            if (word==""):
                continue
            else:
                print(word)
                new_str.append(word)
        new_str.reverse()
        
        new_str=' '.join(new_str)
        return new_str
