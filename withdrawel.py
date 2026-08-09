balance=50000
tot_withdrawal=0
withdrawal_count=0
print('intial balance = Rs.',balance)
while True:
    a=float(input('Enter a withdrawel amount - Rs. '))
    if a==-1:
        break
    elif a<=balance:
        balance=balance - a
        tot_withdrawal=tot_withdrawal+a
        withdrawal_count=withdrawal_count+1

        print('withdrawal successful.remaining balance Rs. ',balance)
    else:
        print('insuffient balance')

print('Remaining balance - ',balance)
print('total amount withdrawn : ',tot_withdrawal)
print('number of successsful withdrawals - ',withdrawal_count)
