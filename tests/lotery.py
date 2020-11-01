from random import randint
numbers = []


while len(numbers) < 6:
    number = randint(1, 61)
    numbers.append(number)


numbers = sorted(numbers)

print("Os Numeros escolhidos são: ")
for n in numbers:
    print(n, end= " | ")
print()
print("Boa Sorte ")