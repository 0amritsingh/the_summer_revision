given_dict = {'rice':50,'wheat':20,'sugar':0,'oil':15,'dal':0}
print('In-Stock Items:', [i[0] for i in list(given_dict.items()) if i[1] > 0])
print('Out-of-Stock Items:', [i[0] for i in list(given_dict.items()) if i[1] == 0])