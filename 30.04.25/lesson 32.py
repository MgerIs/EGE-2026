int() # целые числа
float() # дробные числа, вещественные числа, числа с плавающей точкой
complex()
bool() # логический тип

# Итерируемый объект, Коллекция
# Последовательности
list() # список
str() # строки
tuple() # кортеж

dict() # Словарь
set() # Множество

# Множество - тип коллекции, который содержит уникальные неиндексируемые элементы
my_set = {1, 2, 3}

# add() - добавление элемента в множество
# принимает любой тип данных, кроме списков и словарей
# возвращает None
my_set.add(4)
print(my_set)

# remove() - удаление определенного элемента из множества
# если передать элемент, которого не существует в множестве, будет ошибка
# возвращает None
my_set.remove(1)
print(my_set)

# Объединение множеств
my_set2 = {1, 2, 3}
union_set = my_set.union(my_set2)
print(union_set)

# Разность множеств
diff_set = my_set.difference(my_set2) # 2 3 4
print(diff_set)

# Симметричная разность
sym_diff_set = my_set.symmetric_difference(my_set2)
print(sym_diff_set)

# Отношения между множествами
# issubset() - Проверяет, является ли одно множество подмножеством другого
sub_set = {3, 4, 5}
super_set = {1, 2, 3, 4 ,5 ,6}
print(super_set.issubset(sub_set))
print(sub_set.issubset(super_set))

# issuperset() - Проверяет, является ли одно множество надмножеством другого
print(super_set.issuperset(sub_set))
print(sub_set.issuperset(super_set))