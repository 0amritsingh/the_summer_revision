num = []
for i in range(6):
    ui = int(input(f'Enter number {i + 1}: '))
    num.append(ui)

even_squares = [a**2 for a in num if a%2 == 0]
odd_cubes = [a**3 for a in num if a%2 != 0]
print(even_squares)
print(odd_cubes)