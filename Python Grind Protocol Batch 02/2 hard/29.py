d = {
    'india': 'dehli',
    'nepal': 'kathmandu',
    'pakistan': 'lahore'
}
countryname = list(d.keys())
capitalname = list(d.values())
u = input('Enter city name: ')
if u in capitalname:
    print(f'{u} is a capital')
else:
    print(f'{u} is not a capital')