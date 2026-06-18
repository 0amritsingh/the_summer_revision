students = {}
for i in range(5):
    name = input('Enter name of the student: ')
    marks = int(input(f'Enter marks of {name}: '))
    students.update({name: marks})
print('\nReport of all students: ')
for i in students:
    if students.get(i) >= 40:
        result = 'Pass'
    else:
        result = 'Fail'
    print(f'\nName: {i}\nMarks: {students.get(i)}\nResult: {result}')