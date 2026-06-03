username = input('Enter username: ')
if 5 <= len(username) <= 15:
    if username[0].isalpha() == True:
        if username.find(' ') == -1:
            print('Valid')
        else:
            print('Invalid: Username must not have whitespaces')
    else:
        print('Invalid: Username must start with a letter')
else:
    print('Invalid: Username must be in the range between 5-15')