from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1,dot2) for dot2 in cluster)
        res.append([sum_dist,dot1])
    return min(res)[1]

with open("files/27_B_20911 (1).txt") as file:
    dots = [list(map(float,i.replace(",",".").split())) for i in file]
    cluster1 = [dot for dot in dots if dot[1]>5]
    cluster2 = [dot for dot in dots if -5<dot[1]<5]
    cluster3 = [dot for dot in dots if dot[1]<-5]

center1 = center(cluster1)
center2 = center(cluster2)
center3 =center(cluster3)

print((abs(center1[0]+center2[0]+center3[0]))/3*10000)
print((abs(center1[1]+center2[1]+center3[1]))/3*10000)