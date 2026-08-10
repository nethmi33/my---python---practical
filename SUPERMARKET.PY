item_code=['ITM001','ITM002','ITM003','ITM004','ITM005','ITM006','ITM007','ITM008','ITM009','ITM010']
item_name=['Rice(1 Kg)','sugar(1 Kg)','Milk powder','Bread','EGGS(10 pack)','Butter','Tea (200 g)','Cooking oil(1 l)','Soap','Shampoo']
price=[250,280,1450,180,520,780,650,950,220,890]
print(f'{'Item code': <20} {'item name': <35} {'item price' :20}')
print('='*75)
for i in range(len(item_code)):
    print(f'{item_code[i] :<20} {item_name[i] :<35} {price[i] :<20}')
print('-------------------- SUPERMARKET BILLING SYSTEM ----------------------')
final_bill=0
print(f'{'Item code': <20} {'item name': <35} {'Quantity' :10} {'item price' :12} {'Total' :<10}')
print('='*87)
while True:
    code=input('Enter the item code: ').upper()
    if code in item_code:
        index=item_code.index(code)
        quantity=int(input('Enter the quantity : '))
        tot=quantity*price[index]
        final_bill +=tot
        print(f'{item_code[index]:<20} {item_name[index]:<35} {quantity:<10} {price[index]}')
    else:
        print('invalid item code!')
        print('                                                                        ')
    choise=int(input('Do you want to enter the another item? (1 - yes / 2 - no) : '))
    if choise==2:
        break
    print('='*87)
print(f'{'FINAL BILL AMOUNT (RS.)':<80{final_bill}}')
print('='*87)
