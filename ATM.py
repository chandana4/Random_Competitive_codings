x=input()
bal=input()
if x>0:
    if bal>=0:
        if x%5==0:
            if bal-x-0.5>0:
                bal=bal-x-0.5
                print bal
