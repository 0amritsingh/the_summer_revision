user = 'admin'
pswd = '1234'
username = input('Enter username: ')
passward = input('Enter passward: ')
if user == username and pswd == passward:
    print('Access granted')
else:
    print('Wrong credentials')