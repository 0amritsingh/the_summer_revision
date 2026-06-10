dob = input('Enter you date of birth as \'DD-MM-YYYY\': ')
d = dob[:2]
m = dob[3:5]
y = dob[6:]
a = ''
if d[1] == '1':
    a = 'st'
elif d[1] == '2':
    a = 'nd'
elif d[1] == '3':
    a = 'rd'
else:
    a = 'th'
b = ''
if m == '01':
    b = 'January'
elif m == '02':
    b = 'February'
elif m == '03':
    b = 'March'
elif m == '04':
    b = 'April'
elif m == '05':
    b = 'May'
elif m == '06':
    b = 'June'
elif m == '07':
    b = 'July'
elif m == '08':
    b = 'Augest'
elif m == '09':
    b = 'Septumber'
elif m == '10':
    b = 'October'
elif m == '11':
    b = 'November'
elif m == '12':
    b = 'December'

print(f'Day: {d}\nMonth: {b}\nYear: {y}\n')
message = f'You were born in {y} on the {d+a} of {b}'
print(message)