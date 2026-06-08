op = int(input("Enter original price: "))
if op > 500:
    d = '10%'
    discount = (10/100 * op)
    dp = op - discount
    tax = 18/100 * dp
    fp = dp + tax
else: 
    d = '5%'
    discount = (5/100 * op)
    dp = op - discount
    tax = 18/100 * dp
    fp = dp + tax

print(f'original price:\t{op}\ndiscount({d}):\t{discount}\nfinal price including tax(18%):\t{fp}')
