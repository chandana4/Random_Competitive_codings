t=input()
for i in range(0,t):
    (a,b)=map(int,raw_input().split())
    if a>b:
        print a,a+b
    else:
        print b,a+b
