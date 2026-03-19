from string import printable as alph

for x in alph[:22]:
    c1 = int(f"56{x}C20",22)
    c2 = int(f"89F{x}2",22)
    c3 = int(f"H24{x}K21",22)
    u1 = c1+c2+c3
    if u1%21 == 0:
        print(u1//21)