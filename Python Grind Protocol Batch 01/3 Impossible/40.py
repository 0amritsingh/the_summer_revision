while True:
    pwd = input('Enter a password: ')

    if len(pwd) >= 8:
        if '1234567890' in pwd:
            if 'QWERTYUIOPASDFGHJKLZXCVBNM' in pwd:
                print('Srong Password')
            else:
                print('Weak Password: atleast one uppercase letter')
        else:
            print('Weak Password: atleast one digit')
    else:
        print('Weak Password: lengh must be greater then or equal to 8')
