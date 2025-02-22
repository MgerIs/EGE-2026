# data = "hillo"
# print(data.split('e'))
# print(data.replace("l", "p"))
# s = data.replace("l", "p").replace("h","g")
# print(s)
# print(data.replace("l", "n", 1))
# data1 = "hello hello"
# data2 = data1[::-1].replace("e","p",1).replace("l","o",1)
#
# print(data2[::-1])

# data = "Иванов ИВАН иваныч"
# s = data.replace(" ", ",")
# print(s)



def f(n):
    return int(n[-1])





data = ["4332", '234324', "213"]
print(max(data, key =f))


