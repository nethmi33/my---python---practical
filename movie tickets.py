ticket_p=800
tot_ticket_cost=0
dis=0
pay=0
a=int(input('enter number of movie tickets - '))
if a>5:
    b=int(input('are you have a loyalty card?[if you have card - press 1/if you not have card - press 0]'))
    if b==1:
        dis=ticket_p*a*0.20
        print('you get the 20% Discount')
    else:
        dis=ticket_p*a*0.10
        print('you get the 10% Discount')

else:
    print('you have no discount')

    tot_ticket_cost=ticket_p*a
    pay=tot_ticket_cost-dis


print('total ticket cost - Rs. ',tot_ticket_cost)
print('discount amount - Rs, ',dis)
print('final amount to pay - Rs .',pay)
