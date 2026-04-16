from math import *

def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1,dot2) for dot2 in cluster)
        res.append([sum_dist,dot1])
    return min(res)[1]

with open("files/27_A_23209.txt") as file:
    dots = [list(map(float,i.replace(",",".").split())) for i in file]
    cluster_a1 = [dot for dot in dots if dot[1]<10]
    cluster_a2 = [dot for dot in dots if dot[1]>10]

center_a1 = center(cluster_a1)
center_a2 = center(cluster_a2)


print(max(center_a1[0],center_a2[0])*10000)
print(max(center_a1[1],center_a2[1])*10000)


with open("files/27_B_23209.txt") as file:
    dots = [list(map(float, i.replace(",", ".").split())) for i in file]

cluster1 = [dot for dot in dots if 12>dot[1]>3]
cluster2 = [dot for dot in dots if 21>dot[1]>15]
cluster3 = [dot for dot in dots if 27>dot[1]>21]

center1 = center(cluster1)
center2 = center(cluster2)
center3 = center(cluster3)
clusters = [cluster3,cluster1,cluster2]
center_min = center(min(clusters,key=len))
center_max = center(max(clusters,key=len))
print(int(abs(center_min[0]-center_max[0])*10000))
print(int(abs(center_min[1]-center_max[1])*10000))