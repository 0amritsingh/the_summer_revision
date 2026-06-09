name = input('Enter your name: ')
item1 = input('Enter item 1: ')
price1 = float(input('Enter price: '))
item2 = input('Enter item 2: ')
price2 = float(input('Enter price: '))
item3 = input('Enter item 3: ')
price3 = float(input('Enter price: '))
total = price1+price2+price3
tax = total*0.1

receipt = f"""
======================
  Jatin Kirana Store
======================
Name: {name.title()}
----------------------
Item\tPrice
----------------------
{item1.title()}\t{price1:.2f}
{item2.title()}\t{price2:.2f}
{item3.title()}\t{price3:.2f}
----------------------
Subtotal:\t{total:.2f}
Grand Total:\t{(total+tax):.2f}
(included 10% tax)
======================
Thanks for shopping.
Please visit again!
======================

"""
print(receipt)