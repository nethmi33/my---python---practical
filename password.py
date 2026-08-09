password='admin123'
i=0
while i<3:
    a=str(input('enter password - '))
    if a==password:
        print('login successful')
        break
    else:
        print('wrong password')
        i=i+1

        if i==3:
            print('acccount blocked')
