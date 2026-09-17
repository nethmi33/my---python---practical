Task 2: Add a New Element to an ArrayCreate an array containing 7 integer values.Ask the user to enter a new integer.
Ask the user to enter the index where the new value should be placed.Move the elements from that index one position towards the end of the array.
Store the new value at the specified index.Print the resulting array.



num=[1,2,3,4,5,6,7]
print('original list :',num)
new=int(input('Enter the new value to add : '))
index=int(input('enter index(0 to 7): '))
num.insert(index, new)
print('Updated list :',num)

 
