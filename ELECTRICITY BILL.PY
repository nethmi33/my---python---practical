tot_customer=0
tot_amount=0
while True:
    a=int(input('enter units - '))
    if a==-1:
        break
    elif a<=100:
        bill=a*10
        print('Tot amount is - ',tot_amount)
    elif a>=101 and a<=200:
        bill=(100*10) + ((a-100)*15)
    else:
        bill=(100*10) + (100*15) + ((a-200)*20)
    print('Tot amount is : ',bill)

    tot_customer=tot_cus+1
    tot_amount=tot_amount+bill

if tot_customer>0:
    avg=tot_amount/tot_customer
else:
    avg=0

print('----- summery -----')
print('total number of customers : ',tot_customer)
print('total amount collected : ',tot_amount)
print('average bill amount : ',avg)
