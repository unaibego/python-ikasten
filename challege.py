numbers = [5, 2, 5, 2, 2]
for x in numbers:
    for y in range(x):
        print('*', end="")
    print("")

print("beste aukera bat, hemen aprobetxatuko dugu pythonen stringak gehitu ahal direla")
for x in numbers:
    output = ''
    for y in range(x):
        output += '+'
    print(output)