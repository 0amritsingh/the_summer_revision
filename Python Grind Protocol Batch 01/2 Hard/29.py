c = int(input('Enter temprature in celsius: '))
c = float(c)
f = c*(9/5)+32
k = c + 273.15
print(f'{c: .2f} C is {f: .2f} F \n{c: .2f} C is {k: .2f} K') 
# for two decimal places we use a:. 2f in fstring