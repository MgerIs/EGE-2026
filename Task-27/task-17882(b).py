from math import *


def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]


with open("files/27_B_17882.txt") as file:
    dots = [list(map(float, i.split())) for i in file]

cluster_1 = [dot for dot in dots if dot[1] < 3]
cluster_2 = [dot for dot in dots if 3 < dot[1] < 7]
cluster_3 = [dot for dot in dots if dot[1] > 7]

center1 = center(cluster_1)
center2 = center(cluster_2)
center3 = center(cluster_3)

print((center1[0] + center2[0]+center3[0])/3*10000)
print((center1[1] + center2[1]+center3[1])/3*10000)
