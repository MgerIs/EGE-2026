from itertools import product
cnt = 0
for x in product('ПИТОН', repeat=4):
    s = ''.join(x)
    if 'ИО' not in s and 'ОИ' not in s and 'ОО' not in s and 'ИИ' not in s and 'ПТ' not in s and 'ТП' not in s and 'ТН' not in s \
        and 'НТ' not in s and 'ПН' not in s and 'НП' not in s and 'ПП' not in s and 'НН' not in s and 'ТТ' not in s:
        cnt += 1
print(cnt)