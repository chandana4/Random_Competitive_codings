b=str(raw_input())
b=b.split(",")
one='1'
zero='0'
two='2'
a=[]
if one in b:
    a.append('1')
    b.remove('1')
    if two in b:
        a.append('2')
        b.remove('2')
    elif one in b:
        a.append('1')
        b.remove('1')
    elif zero in b:
        a.append('0')
        b.remove('0')
    else:
        print 0
else:
    if zero in b:
        a.append('0')
        b.remove('0')
    else:
        print 0
a.append("/")
three='3'
if (three and one)in b:
    a.append('3')
    b.remove('3')
    a.append('1')
    b.remove('1')
elif (three and zero) in b:
    a.append('3')
    b.remove('3')
    a.append('0')
    b.remove('0')
elif two in b:
    a.append('2')
    b.remove('2')
    a.append(str(max(b)))
    b.remove(str(max(b)))
elif one in b:
    a.append('1')
    b.remove('1')
    a.append(str(max(b)))
    b.remove(str(max(b)))
elif zero in b:
    a.append('0')
    b.remove('0')
    a.append(str(max(b)))
    b.remove(str(max(b)))
else:
    print 0
a.append(" ")
four='4'
if (two and four) in b:
    a.append('2')
    b.remove('2')
    a.append('4')
    b.remove('4')
elif (two and three) in b:
    a.append('2')
    b.remove('2')
    a.append('3')
    b.remove('3')
elif (two and two) in b:
    a.append('2')
    b.remove('2')
    a.append('2')
    b.remove('2')
elif (two and one) in b:
    a.append('2')
    b.remove('2')
    a.append('1')
    b.remove('1')
elif (two and zero) in b:
    a.append('2')
    b.remove('2')
    a.append('0')
    b.remove('0')
elif one in b:
    a.append('1')
    b.remove('1')
    a.append(str(max(b)))
    b.remove(str(max(b)))
elif zero in b:
    a.append('0')
    b.remove('0')
    a.append(str(max(b)))
    b.remove(str(max(b)))
else:
    print 0
a.append(":")
five='5'
if five in b:
    a.append('5')
    b.remove('5')
    a.append(str(max(b)))
    b.remove(str(max(b)))
elif four in b:
    a.append('4')
    b.remove('4')
    a.append(str(max(b)))
    b.remove(str(max(b)))
elif three  in b:
    a.append('3')
    b.remove('3')
    a.append(str(max(b)))
    b.remove(str(max(b)))
elif two in b:
    a.append('2')
    b.remove('2')
    a.append(str(max(b)))
    b.remove(str(max(b)))
elif one in b:
    a.append('1')
    b.remove('1')
    a.append(str(max(b)))
    b.remove(str(max(b)))
elif zero in b:
    a.append('0')
    b.remove('0')
    a.append(str(max(b)))
    b.remove(str(max(b)))
else:
    print 0
str1 = ''.join(a)
print str1
