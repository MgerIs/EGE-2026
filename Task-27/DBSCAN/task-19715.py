from math import *



def center(cluster):
    res = []
    for dot1 in cluster:
        sum_dist = sum(dist(dot1, dot2) for dot2 in cluster)
        res.append([sum_dist, dot1])
    return min(res)[1]


with open("27.21.A_19715.txt") as file:
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
print(centers)
print((centers[0][0]+centers[1][0])/2*10000)
print((centers[0][1]+centers[1][1])/2*10000)

with open("../files/27.21.B_19715.txt") as file:
    dots = [list(map(float, i.replace(",", ".").split())) for i in file]

eps = 4
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
print(centers)
print(abs(centers[0][0]+centers[1][0]+centers[2][0]+centers[3][0])/4*10000)
print(abs(centers[0][1]+centers[1][1]+centers[2][1]+centers[3][1])/4*10000)