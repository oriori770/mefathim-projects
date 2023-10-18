import random


class MinHeap:

    def __init__(self, arr=None):
        self.heap = arr
        self.__build_heap()

    def insertion(self, number):
        self.heap.append(number)
        self.min_heapify(-1)

    def get_size(self):
        return len(self.heap)

    def checking_is_not_empty(self):
        return self.get_size()

    # def
    def __build_heap(self):
        for i in range(self.get_size()//2 + 1, -1, -1):
            self.min_heapify(i)

    def min_heapify(self, index):
        left = index * 2
        right = index * 2 + 1
        if left < self.get_size() and self.heap[left] < self.heap[index]:
            smallest = left
        else:
            smallest = index
        if right < self.get_size() and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest],  self.heap[index]
            self.min_heapify(smallest)

    def extraction_of_the_minimum(self):
        if not self.checking_is_not_empty():
            return ''
        min_in_heap = self.get_minimum_element()
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.min_heapify(0)
        return min_in_heap

    def get_minimum_element(self):
        return self.heap[0]

    def __str__(self):
        return self.heap.__str__()


# a = [random.randint(-100, 100)for i in range(20)]
# print(a)
# b = MinHeap(a)
# print(b.get_minimum_element())
# print(b.heap)
# print(b.get_size())
# print(b.get_minimum_element())
# print(b.checking_is_not_empty())
# print(b.extraction_of_the_minimum())
# print(b.heap)
# b.insertion(7)
# print(b.heap)
