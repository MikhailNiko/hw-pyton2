n = int(input('Введите количество первого множества'))
m = int(input('Введите количество второго множества'))

list_1 = []
list_2 = []

for i in range (0, n):
    element_list_1 = int(input('Введите элементы первого множества'))
    list_1.append(element_list_1)
    
for i in range (0, m):
    element_list_2 = int(input('Введите элементы второго множества'))
    list_2.append(element_list_2)

set_1 = set(list_1)
set_2 = set(list_2)
print(sorted(set_1))
print(sorted(set_2))