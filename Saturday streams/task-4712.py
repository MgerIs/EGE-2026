data = open('26_4712.txt')
n = data.readline()
boxes = sorted([int(i) for i in data])
boxesnew = boxes[::-1]
answer = [boxesnew[0]]
for box in boxesnew[1:]:
    if answer[-1] - box >= 3:
        answer.append(box)
print(len(answer), answer[-1])