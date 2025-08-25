from re import finditer, match

# with open(f'Regexp contest/regexp-practice-1.txt') as file:
#     data = file.read()
#     print(data)
#     pattern = r"\b[Cc][Aa][tT]\b"
#     matches = [match.group() for match in finditer(pattern,data)]
#     print(matches)

# with open(f'Regexp contest/regexp-practice-2.txt') as file:
#     data = file.readlines()
#     pattern =r'[Aa].+'
#     for line in data:
#         if match(pattern,line) != None:
#             print(match(pattern,line).group())

# with open(f'Regexp contest/regexp-practice-3.txt') as file:
#     data = file.read()
#     pattern = r"[0-9]+(\.[0-9]+|[0-9]*)"
#     matches = [match.group() for match in finditer(pattern, data)]
#     print(matches)

# with open(f'Regexp contest/regexp-practice-4.txt') as file:
#     data = file.read()
#     pattern = r"[0-9]+-[0-9]+-[0-9]+"
#     matches = [match.group() for match in finditer(pattern, data)]
#     print(matches)


# with open(f'Regexp contest/regexp-practice-5.txt', encoding="utf-8") as file:
#     data = file.read()
#     pattern = r"[A-ZА-ЯЁ][a-zа-яё]*\b"
#     matches = [match.group() for match in finditer(pattern, data)]
#     print(matches)
# with open(f'Regexp contest/regexp-practice-6    .txt', encoding="utf-8") as file:
#     data = file.read()
#     pattern = r"[A-ZA-ЯЁ]{2}-\d{4}"
#     matches = [match.group() for match in finditer(pattern, data)]
#     print(matches)

# with open(f'Regexp contest/regexp-practice-8.txt', encoding="utf-8") as file:
#     data = file.read()
#     pattern = r"(?:\+?7|8)\s?\(?(\d{3})\)?\s?(\d{3})(?:[- ]?(\d{2})[- ]?(\d{2})|(\d{4}))"
#     matches = [match.group() for match in finditer(pattern, data)]
#     print(matches)


# with open(f'Regexp contest/regexp-practice-9.txt', encoding="utf-8") as file:
#     data = file.read()
#     must_1 = r"(?<=<a href=)"
#     must_2 = r'">'
#     pattern = fr'(?<={must_1}).+?(?={must_2})'
#     matches = [match.group() for match in finditer(pattern, data)]
#     print(matches)

# with open(f'Regexp contest/regexp-practice-10.txt', encoding="utf-8") as file:
#     data = file.read()
#     mat2 = []
#     mat3 = []
#     pattern = r"[0-9]+[- _]+"
#     matches = [match.group() for match in finditer(pattern, data)]
#     print(matches)

# with open(f'Regexp contest/regexp-practice-11.txt', encoding="utf-8") as file:
#     data  = file.read()
#     pattern = r"<[^>]+?>"
#     matches = [match.group() for match in finditer(pattern, data)]
#     print(matches)
#
# with open(f'Regexp contest/regexp-practice-12.txt', encoding="utf-8") as file:
#     data = file.read()
#     mat2 = []
#     pattern = r"[a-zA-Z_-]+@[a-zA-Z-_]+\.\w+"
#     matches = [match.group() for match in finditer(pattern, data)]
#     print(matches)
#     lowercase = [s.lower() for s in matches]
#     print(lowercase)

# with open(f'Regexp contest/regexp-practice-13.txt', encoding="utf-8") as file:
#     data = file.read()
#     pattern = r"\b(\w+)(\s\1)+\b"
#     matches = [match.group() for match in finditer(pattern, data)]
#     print(matches)


with open(f'Regexp contest/regexp-practice-14.txt', encoding="utf-8") as file:
    data = file.read()
    pattern = r"([A-ZА-ЯЁ][a-zа-яё]+ [A-ZА-ЯЁ][a-zа-яё]+ [A-ZА-ЯЁ][a-zа-яё]+)"
    matches = [match.group() for match in finditer(pattern, data)]
    print(matches)

# with open(f'Regexp contest/regexp-practice-15.txt', encoding="utf-8") as file:
#     data = file.read()
#     pattern = r""
#     matches = [match.group() for match in finditer(pattern, data)]
#     print(matches)


