# Методы обработки списков
# Списки нельзя копировать как обычные переменные (числа, строки)
# При копировании списка таким образом будет происходить дублирование
# ссылки на область памяти, где хранится список
a = [1]
b = a
a +=[8]
print(a,b)
print(id(a))
print(id(b))

# append() - добавление одного элемента в конец списка
test_list = [1, 2, 3]
test_list.append(5)
print(test_list)
#extend() - добавляет один список целиком в конец другого
test_list_2 = [1, 5, 7]
test_list_2.extend(test_list_2)
print(test_list_2)
# insert - добавляет один элемент в список на определенную позицию
test_list.insert(3, 4)
print(test_list)
#remove - удаляет первый попавшийся элемент из списка
test_list.remove(2)
print(test_list)
#pop - удаляет элемент на указанной позиции и возвращает его
test = test_list.pop(3)
print(test_list, test)
#index - возвращает позицию указанного элемента
int = test_list.index(1)
print(int)
#count - возвращает кол-во элементов заданного обьекта
cnt = test_list.count(5)
print(cnt)
#copy - копирует список
test_list_3 = test_list.copy()
print(test_list_3)
#clear - очищает список
test_list_3.clear()
print(test_list_3)
#sort - сортирует список
test_list_2.sort()
print(test_list_2)
#reverse - переворачивает список
test_list_2.reverse()
print(test_list_2)
#Математические функции
summ = sum(test_list_2)
minn = min(test_list_2)
maxx = max(test_list_2)


