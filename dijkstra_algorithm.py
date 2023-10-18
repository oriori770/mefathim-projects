# -*- coding: utf-8 -*-
"""Dijkstra algorithm.ipynb

Automatically generated by Colaboratory.

"""
import heapq
import cv2
import matplotlib
import matplotlib.pyplot as plt
from Node_Dijkstra import Node_Dijkstra

# import numpy as np
# import heapq as heap

# file = 'maze.png'
file = 'maze5.jpg'

img = cv2.imread(file)  # read an image from a file using
cv2.circle(img, (5, 220), 3, (255, 0, 0), -1)  # add a circle at (5, 220)
cv2.circle(img, (25, 5), 3, (0, 0, 255), -1)  # add a circle at (5,5)
plt.figure(figsize=(7, 7))
plt.imshow(img)  # show the image
img = cv2.imread(file)
plt.show()

start_point = (330, 40)  # y = 5, x = 25
end_point = (330, 330)  # y = 220, x = 5
# start_point = (5, 25) # y = 5, x = 25
# end_point = (220, 5) # y = 220, x = 5
print(img.shape)

root_2 = 2 ** (1 / 2)
true_false_matrix = (img[:, :, 0]) > 200
height_matrix = len(img)  # the max y 689
width_matrix = len(img[0])  # the max x 564
# neighbors_matrix = [[[] for i in range(height_matrix)] for j in range(width_matrix)]
parent_matrix = [[[None] for i in range(width_matrix)] for j in range(height_matrix)]
weight_matrix = [[float('inf') for i in range(width_matrix)] for j in range(height_matrix)]
visited_matrix = [[[False] for i in range(width_matrix)] for j in range(height_matrix)]


def dijkstra(img, start_point, end):
    heap = []
    sx, sy = start_point
    ex, ey = end
    heapq.heappush(heap, (0, start_point))
    current = (sx, sy)
    cx, cy = current
    weight_matrix[cx][cy] = 0
    while not visited_matrix[ex][ey][0]:
        cx, cy = current
        for neighbors in find_edge(cx, cy):
            nx, ny = neighbors
            if visited_matrix[nx][ny][0]:
                continue
            new_weight = weight_matrix[cx][cy] + set_weight(cx, cy, nx, ny)
            if new_weight < weight_matrix[nx][ny]:
                weight_matrix[nx][ny] = new_weight
                parent_matrix[nx][ny] = current
                heapq.heappush(heap, (new_weight, neighbors))
        visited_matrix[cx][cy][0] = True
        if len(heap) > 0:
            _, current = heapq.heappop(heap)


def create_path():
    pat = []
    node = end_point
    while node != start_point:
        pat.append(node)
        node = parent_matrix[node[0]][node[1]]
    return pat


def set_weight(source_x, source_y, destination_x, destination_y):
    if source_x == destination_x or source_y == destination_y:
        return 1
    else:
        return root_2


def find_edge(x, y):
    edge = []
    neighbors = [(x, y + 1), (x, y - 1), (x + 1, y), (x + 1, y + 1),
                 (x + 1, y - 1), (x - 1, y), (x - 1, y + 1), (x - 1, y + 1)]
    for point in neighbors:
        if 0 < point[0] < height_matrix and 0 < point[1] < width_matrix:
            # Maybe the length and width should be reversed
            if true_false_matrix[point]:
                edge.append(point)
    return edge


def drawPath(img, path, thickness=1):
    """path is a list of (x,y) tuples"""
    x0, y0 = path[0]
    for vertex in path[1:]:
        x1, y1 = vertex
        cv2.line(img, (y0, x0), (y1, x1), (255, 0, 0), thickness)
        x0, y0 = vertex


dijkstra(img, start_point, end_point)
path = create_path()
drawPath(img, path)
# plt.figure(figsize=(7, 7))
plt.imshow(img)  # show the image on the screen
plt.show()
# print(len(true_false_matrix))
# print(len(img))
print(len(true_false_matrix[0]))
# print(len(img[0]))