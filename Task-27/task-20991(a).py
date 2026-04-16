from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1,dot2) for dot2 in cluster)
        res.append([sum_dist,dot1])
    return min(res)[1]

with open("files/27_A_20911 (1).txt") as file:
    dots = [list(map(float,i.replace(",",".").split())) for i in file]
    cluster1 = [dot for dot in dots if dot[1]<0]
    cluster2 = [dot for dot in dots if dot[1]>0]

center1 = center(cluster1)
center2 = center(cluster2)

print((abs(center1[0]+center2[0]))/2*10000)
print((abs(center1[1]+center2[1]))/2*10000)