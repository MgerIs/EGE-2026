# Словари - тип коллекций, которых хранит в себе неиндексированный
# итерируемый набор элементов в формате "ключ:значение".
# Словари являются отдельным типом коллекций,
# который называется отображением (mapping).

my_dict = {'name':'Artyom', 'age':16}
print(my_dict['name'])

my_list1 = [] # создание списка
my_list2 = list()
print(type(my_list1), type(my_list2))

my_tuple1 = () # создание кортежа
my_tuple2 = tuple()
print(type(my_tuple1), type(my_tuple2))

my_set1 = {} # создание словаря
my_set2 = set()
print(type(my_set1), type(my_set2))

# keys() - все ключи словаря
print(my_dict.keys())

# values() - все значения словаря по порядку
print(my_dict.values())

# items() - все связки ключ + значение
print(my_dict.items())

# добавление элемента в словарь
my_dict['lastname'] = 'Ivanov'
print(my_dict)

# удаление элемента из словаря
a = my_dict.pop('lastname')
print(my_dict)

# извлечение элемента из словаря
b = my_dict.get('age')
print(b)



with open('26_17565.txt') as file:
    N, S = map(int, file.readline().split())
    sailors = {}
    for i in file:
        sailor = list(map(int, i.split()))
        sailors[sailor[0]] = (sum(sailor[1:-1]), sailor[-1])

sailors_2 = sorted(sailors, key=lambda x: (sailors[x], -x), reverse=True)

last_passed = sailors_2[S - 1]
first_not_passed = sailors_2[S]
if sailors[last_passed][0] == sailors[first_not_passed][0]:
    half_point = sailors[last_passed][0]
    last_sailor_ID = 0
    cnt_half_point = 0
    for id in sailors_2:
        if sailors[id][0] == half_point:
            cnt_half_point += 1
        if sailors[id][0] > half_point:
            last_sailor_ID = id
    print(last_sailor_ID, cnt_half_point)
