marks=[]
for i in range(1,6):
    a=int(input(f'enter marks {i} : '))
    marks.append(a)
print('all marks : ',marks)
tot=sum(marks)
avg=tot/len(marks)
print('total marks : ',tot)
print('average marks : ',avg)
high=max(marks)
low=min(marks)
print('highets mark : ',high)
print('lowest mark : ',low)

count=0
for a in marks:
    if a<50:
        count+=1
print('subjects have marks below 50 : ',count)
if avg>75:
    grade='A'
elif avg>60 and avg<74:
    grade='B'
elif avg>50 and avg<59:
    grade='C'
else:
    grade='F'

print('grade : ',grade)
