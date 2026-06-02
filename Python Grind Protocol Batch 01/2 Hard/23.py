while True:
    username = input('Enter your username: ')
    # print(len(username))
    if 5 >= len(username) <= 15:
        print('Valid')
        if username[0].isalpha() == True:
            print('Valid')
            if username.find(' ') == 0:
                print('Valid')
            # else:
            #     print('Invaild')
        # else:
        #     print('Invaild')
    else:
        print('Invaild')