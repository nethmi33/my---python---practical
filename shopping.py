tot=0
dis=0
x=float(input('Enter the shopping amount - '))
if x >=10000:
    a=int(input('Are you have a membership card? (if you have a card press 1/ if you not have a card press 0 )'))
    if a==1:
        dis=x*0.15
        tot=x-dis
        print('you get the 15% Discount')
    else:
        dis=x*0.10
        tot=x-dis
        print('you get the 10% Discount')
    print('your discount amount - ',dis)
    print('your final amount to pay - ',tot)
