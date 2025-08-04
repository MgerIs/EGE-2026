# Считать с клавиатуры строку text.
# Считать строку old (что мы хотим заменить).
# Считать строку new (на что мы хотим заменить).
# Заменить первое вхождение old на new.

text = input('Введите строку: ')
old = input('Введите подстроку, которую нужно заменить: ')
new = input('Введите подстроку, которой нужно заменить: ')
cnt = int(input())

while old in text and cnt > 0:
    index_old = text.index(old)
    text_before_old = text[:index_old]
    text_after_old = text[index_old + len(old):]
    text = text_before_old + new + text_after_old
    cnt -= 1
print(text)