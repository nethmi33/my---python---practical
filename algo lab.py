num=[1,2,3,4,5,6,7]
print('original list :',num)
new=int(input('Enter the new value to add : '))
index=int(input('enter index(0 to 7): '))
num.insert(index, new)
print('Updated list :',num)
