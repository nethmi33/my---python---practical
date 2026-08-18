students=[]
print('Enter details for 7 students:')
print('-----------------------------------')
for i in range(7):
    a=input('Enter student name : ')
    s1=float(input('Enter subject 1 marks : '))
    s2=float(input('Enter subject 2 marks : '))
    s3=float(input('Enter subject 3 marks : '))
    print('                                 ')
    tot=s1+s2+s3
    avg=tot/3
    students.append([a,s1,s2,s3,tot,avg])


print('\n'+ '='*50)
print('student details')
print('-----------------------------------')

for student in students:
    print(f'Name: {student[0]}, Total: {student[4]}, Average: {student[5]:.2f}')

students.sort(key=lambda x:x[5],reverse=True)
print('                                    ')
print('Ranked list:')
print('='*50)
print(f'{'Rank' :<4} {'Name' :<10} {'Total' :<8} {'Average'}')
print('='*50)

for i in range (len(students)):
    print(i + 1, students[i][0], students[i][5])

print('                                    ')
print('student who passed all subjects')
print('-----------------------------------')
for student in students:
    if student[1]>=50 and student[2]>=50 and student[3]>=50:
        print(student[0])