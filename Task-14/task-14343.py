for x in range(1,15000):
    num = 5*343**2031 + 4*49**2142 - 3*7**11 + 7**222
    if num % 7 == 0:
        print(x,num//7)