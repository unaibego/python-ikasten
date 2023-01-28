names = ["unai", "Begoña", "Alvarez"]
names.append("Larrabe")
names.insert(0, "Nire izena: ")
names[1] = "Unai"
print(names[:])
names.remove("Alvarez")
names.pop()
print(len(names))
names2 = names
print(names2)
names.clear()
print(" a ver q sale", names)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix[0][1] = 20
print(matrix[0][1])
print(matrix)
#ariketa
number = [1 ,4, 2 , 3 , 4, 5, 5]
for i in number:
    if number.count(i) > 1:
        number.remove(i)
print(number)