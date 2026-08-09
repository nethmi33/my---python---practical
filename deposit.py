tot=0
num=0
high=0
while True:
    a=float(input('enter amount - '))
    if a==0:
        break
    elif a>100000:
        high=high+1
        print('large deposit')
    elif a>=50000 and a<=100000:
        print('medium deposit')
    else:
        print('small deposit')

    num=num+1
    tot=tot+a

print('toal amount : ',tot)
print('number of deposit - ',num)
print('highest deposit amount - ',high)
