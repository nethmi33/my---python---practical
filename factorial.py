import math
a=int(input('Enter the number : '))
if a<=1:
    print(f'{a} is not prime')
elif a==2:
    print(f'{a} is prime')
else:
        is_prime=True
        for i in range(2, int(math.sqrt(a)) +1):
             if a%i==0:
                  is_prime=False
                  break

        if is_prime:
             print(f'{a} is prime')
        else:
             print(f'{a} is not prime')
                
        