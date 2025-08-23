#строки


# получение численного значения символа
print(ord("A"))



# получение символа из численного значения
print(chr(228))

# при сравнении строк, сравнинваются только цифровые значения первых сииволов


if 'AZ' < 'ZA':
    print("+")


a = input()
counters = [0] * 26
for i in a:
    pos = ord(i) - ord("a")
    counters[pos] += 1




max_pos = 0
max_num = 0
for i in range(26):
    if counters[i] > max_num:
        max_num = counters[i]
        max_pos = i



print(chr(max_pos+ ord("a")))





print(chr(counters.index(max(counters)) + ord("a")))







