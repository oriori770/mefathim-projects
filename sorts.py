import time
import random
import matplotlib.pyplot as plt
from HeapSort import heapsort


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


def counting_sort(arr):
    if len(arr) == 0:
        return arr
    range_arr = max(arr) - min(arr) + 1
    index_arr = [0] * range_arr
    sorted_arr = [0 for i in range(len(arr))]

    for i in arr:
        index_arr[i - min(arr)] += 1
    for i in range(1, range_arr):
        index_arr[i] += index_arr[i - 1]
    # for idx, i in enumerate(arr):
    for i in arr:
        sorted_arr[index_arr[i - min(arr)] - 1] = i
        index_arr[i - min(arr)] += -1
    return sorted_arr


# print(counting_sort([5,3,-4,4,0,-3,4,-5]))
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[j], array[i] = array[i], array[j]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(arr):
    quick_sort_recursive(arr, 0, len(arr) - 1)


def quick_sort_recursive(array, start, end):
    if start < end:
        pivot_index = partition(array, start, end)
        quick_sort_recursive(array, start, pivot_index - 1)
        quick_sort_recursive(array, pivot_index + 1, end)


# a = [5, 3, -4, -14, 1, 3, 7, 12, 13, 4, 15, 0, -3, 4, -5, 5]
# quick_sort(a)
# p = partition(a, 0, len(a) - 1)
# print(a)
# print(p)
# print(a)
# print(partition(a,0,len(a)-1))
# #
# def partition(arr, low, high):
#     pivot = arr[high]
#     index_pivot = low
#     for j, i in enumerate(arr[low:high + 1]):
#         if i < pivot:
#             arr[j], arr[index_pivot] = arr[index_pivot], arr[j]
#             index_pivot += 1
#     arr[index_pivot], arr[high] = arr[high], arr[index_pivot]
#
# print(a)
# print(partition(a, 0, len(a)))
# print(a)
# print(quick_sort(a))
# a[0], a[9] = a[9], a[0]
# print(a)


def bubble_sort(arr):
    length = len(arr)
    for j in range(length - 1, 0, -1):
        for i in range(j):
            if arr[i] > arr[i + 1]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
    return arr


def merge_sort(arr):
    def merge(arr, left, mid, right):
        pass

    def merge_sort_helper(arr, left, right):
        pass

    return arr


def radix_sort(arr):
    return arr


#  Test function to verify sorting algorithms
def test_sorting_algorithm(sort_func, n=10):
    # Perform n random test cases
    for _ in range(n):
        length = random.randint(10, 100)
        arr = [random.randint(100, 100_000) for _ in range(length)]
        expected = sorted(arr)
        # Verify that the sorted array matches the expected result
        assert sort_func(arr) == expected

    print("All test cases passed")


test_sorting_algorithm(insertion_sort)
length = 10
random.sample(range(length ** 3), length)


# Function to plot the performance of sorting algorithms
def plot_sorting_performance(algorithms):
    # Define the lengths of arrays for performance testing
    lengths = [100, 500, 1_000, 5_000, 10_000, 15_000, 20_000]
    for algo_name, algo_func in algorithms.items():
        execution_times = []
        for length in lengths:
            arr = random.sample(range(length ** 3), length)
            start_time = time.time()
            algo_func(arr)
            end_time = time.time()
            execution_times.append(end_time - start_time)

        # Plot the execution times for each array length
        plt.plot(lengths, execution_times, label=algo_name)

    plt.xlabel("Array Length")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.show()


algorithms = {"insertion sort": insertion_sort, "bubble sort": bubble_sort, "heap sort": heapsort,
              "quick sort": quick_sort}
# test_sorting_algorithm(counting_sort, 100000)


plot_sorting_performance(algorithms)
