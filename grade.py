def get_grade(average):
    if average>=75:
        return 'A'
    elif average >=65:
        return 'B'
    elif average>=55:
        return 'C'
    elif average>=40:
        return 'S'
    else:
        return 'F'

def get_comment(grade):
    comments={
        'A' : 'Excellent! keep it up!',
        'B' : 'Good job!',
        'C' : 'Satisfactory, can do better.',
        'D' : 'Just passed.Need to improve.',
        'F' : 'Failed.Work harder next time.'
    }

    return comments[grade]
name=input('Enter student name : ')
marks=[]
for i in range(1,6):
    mark=float(input(f'Enter marks for subject{i} :'))
    marks.append(mark)
average=sum(marks)/5
grade=get_grade(average)
student_data={
    'Name' : name,
    'Marks' : marks,
    'Average' : round (average,2),
    'Grade' : grade,
    'Comment' : get_comment(grade)
}
print('----- student result -----')
print(f'Name : {student_data['Name']}')
print(f'Marks : {student_data['Marks']}')
print(f'Average : {student_data['Average']}')
print(f'Grade : {student_data['Grade']}')
print(f'Comment : {student_data['Comment']}')
