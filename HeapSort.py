import random
from MinHeap import MinHeap


def heapsort(array):
    b = MinHeap(array[:])
    for i in range(len(array)):
        array[i] = b.extraction_of_the_minimum()


# a = [random.randint(-100, 100)for i in range(20)]
# b = sorted(a[:])
# # print(a)
# heapsort(a)
# if not a == b:
#     print(a)
#     print(b)
# else:
#     print("Great!")
