from math import *


def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]


with open("../files/27_A_23209.txt") as file:
    dots = [list(map(float, i.replace(",", ".").split())) for i in file]

eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 30:
        clusters.append(cluster)
print([len(cluster) for cluster in clusters])
centers = [center(cluster) for cluster in clusters]

print(max(centers, key=lambda x: x[0])[0] * 10000)
print(max(centers, key=lambda x: x[1])[1] * 10000)



################################################


with open("../files/27_B_23209.txt") as file:
    dots = [list(map(float, i.replace(",", ".").split())) for i in file]

eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 30:
        clusters.append(cluster)
print([len(cluster) for cluster in clusters])
centers = [center(cluster) for cluster in clusters]
center_min = center(min(clusters,key=len))
center_max = center(max(clusters,key=len))
print(int(abs(center_min[0]-center_max[0])*10000))
print(int(abs(center_min[1]-center_max[1])*10000))