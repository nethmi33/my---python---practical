marks=[78,85,92,64,59,85,45]
marks.append(90)
count=0
for mark in marks:
    if mark>=75:
        count +=1
print('students:',count)