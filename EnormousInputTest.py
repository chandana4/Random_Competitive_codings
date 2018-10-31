(num,div)=map(int, raw_input().split()) #takes astring,splits into list and makes every list interger
count=0
l=[]
for i in range(0,num):
    l.append(input())    
    if l[i]%div==0:
        count=count+1

print count
