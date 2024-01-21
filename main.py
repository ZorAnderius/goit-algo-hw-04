from timeit import timeit
import random

from insertion_sort import insertion_sort
from merge_sort import merge_sort

def main():
    data_small = [random.randint(0, 100_000) for _ in range(1_000)]
    data_medium = [random.randint(0, 1_000_000) for _ in range(10_000)]
    data_large = [random.randint(0, 1_000_000) for _ in range(100_000)]

    
    time_small_insertion = timeit(lambda: insertion_sort(data_small[:]), number=5)
    time_small_merge = timeit(lambda: merge_sort(data_small[:]), number=5)
    time_small_sorted = timeit(lambda: sorted(data_small[:]), number=5)
    time_small_sort = timeit(lambda: data_small[:].sort(), number = 5)
    
    time_medium_insertion = timeit(lambda: insertion_sort(data_medium[:]), number=5)
    time_medium_merge = timeit(lambda: merge_sort(data_medium[:]), number=5)
    time_medium_sorted = timeit(lambda: sorted(data_medium[:]), number=5)
    time_medium_sort = timeit(lambda: data_medium[:].sort(), number = 5)
    
    time_large_insertion = timeit(lambda: insertion_sort(data_large[:]), number=5)
    time_large_merge = timeit(lambda: merge_sort(data_large[:]), number=5)
    time_large_sorted = timeit(lambda: sorted(data_large[:]), number=5)
    time_large_sort = timeit(lambda: data_large[:].sort(), number = 5)
    
    print(f"{'|  Algorithm type': <16} |  {'Time (data: 1 000)': <16} |{'Time (data: 10 000)': <16} |{'Time (data: 100 000)': <18}")
    print(f"|{'-'*16} | {'-'*19} | {'-'*18} | {'-'*18}")
    print(f"{'|  Insertion sort': <17} | {time_small_insertion: <19.5f} | {time_medium_insertion: <18.5f} | {time_large_insertion: <20.5}")
    print(f"{'|  Merge sort': <17} | {time_small_merge: <19.5f} | {time_medium_merge: <18.5f} | {time_large_merge: <20.5}")
    print(f"{'|  Sorted': <17} | {time_small_sorted: <19.5f} | {time_medium_sorted: <19.5f}| {time_large_sorted: <20.5}")
    print(f"{'|  Sort': <17} | {time_small_sort: <19.5f} | {time_medium_sort: <18.5f} | {time_large_sort: <20.5}")
 

if __name__ == '__main__':
    main()