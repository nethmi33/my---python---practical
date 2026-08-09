medicine_code=['MED001','MED002','MED003','MED004','MED005','MED006','MED007','MED008','MRD009','MED010']
medicine_name=['Paracetamol','Vitamin c','Cough syrup','Antacid','Pain relief gel','Face mask pack','Hand sanitizer','Bandage  roll','Antibiotic cream','Digital thermometer']
medicine_price=[120,450,780,350,920,180,520,250,680,2150]
print(f'{'medicine-code' : <20} {'medicine_name':35} {'medicine_price' :20}')
print('-'*75)
for i in range (len (medicine_code)):
    print(f'{medicine_code[i]   :<20} {medicine_name[i]   :<35} {medicine_price   [i]  :<20}')

print('-------PHAMARCY BILLING SYSTEM-------')
final_bill=0
print(f'{'code':<15} {'medicine name':<40}{'quantity':<12}{'unit price':<20}{'Total':<15}')
print('-'*102)
while True:
    code=input('Enter medicine code - ').upper()
    if code in medicine_code:
        index=medicine_code.index(code)
        quantity=int(input('Enteer quantity - '))
        total=quantity*medicine_price[index]
        final_bill +=total
        print(f'{medicine_code[index]:<15} {medicine_name[index]:<40} {quantity:<8}{medicine_price[index]}')
    else:
        print('Invalid medicicne code !')
    choise=input('Do you want to add another medicine ? (Y/N) - ').upper()
    if choise=="N":
        break
    print("-"*102)
print(f'{"Final Bill Amount (Rs.)":<65}{final_bill}')
print("-"*102)

