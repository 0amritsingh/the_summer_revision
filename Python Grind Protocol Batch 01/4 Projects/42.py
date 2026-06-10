name = input("Enter full name: ")
age = int(input('Enter age(in numeric): '))
city = input("Enter your city: ")
username = input('Enter username (must be >= 4 chars, no space): ')
password = input('Enter password (must be >= 6 chars, no space): ')

status = ""
if age > 18:
    status = 'Adult'
else:
    status = 'Minor'

if len(username) >= 4 and username.find(' ') == -1:
    if len(password) >= 6 and password.find(' ') == -1:
        print('\nSuccess! now you can login')
    else:
        print('\nError: password must be >= 6 chars with no space')
        exit()
else:
    print('\nError: username must be >= 4 chars with no space')
    exit()

print("\nLOGIN\n")
u = input('Enter username: ')
p = input('Enter password: ')

profile =f"""
-----------------------
USER PROFILE
-----------------------
username: {username}
-----------------------
Name\t{name.title()}
Age\t{age}({status})
City\t{city.upper()}
-----------------------"""
if username == u and password == p:
    print(profile)
else:
    print('\nError: username or password is invaild')