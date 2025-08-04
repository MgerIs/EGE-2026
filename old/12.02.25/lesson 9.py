a = input()
count = [0] * 128

for i in a:
    count[ord(i)] += 1

maxx = 0
for i in count:
    if maxx < i:
        maxx = i

for i in range(128):
    if maxx == count[i]:
        print(chr(i))
        break
