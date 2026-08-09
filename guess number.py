num=25
i=0
attempt=0
while True:
    a=int(input('guess number - '))
    if a==25:
        break
    elif a>25:
        print('too high')
    elif a<25:
        print('too low')
    else:
        print('correct guess')
    i=i+1
    attempt=attempt+1
print('number of attempts used - ',attempt)
