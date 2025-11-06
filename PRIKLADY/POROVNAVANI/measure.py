import time
import random
import copy

import matplotlib.pyplot as plt

from bubble1 import bubble1
from bubble2 import bubble2
from bubble3 import bubble3
from bubble4 import bubble4
from insert_sort import insert_sort
from select_sort import select_sort
from quick_sort import quick

def measure_sorts():
    lists_lens = [n for n in range (10,200,10)]

    bubble1_res = []
    bubble2_res = []
    bubble3_res = []
    bubble4_res = []
    insert_res = []
    select_res = []
    quick_res = []

    for n in range(10,200,10):
        unsorted_list = [random.randint(0,n**2) for i in range (n)]

        bubble1_res.append(bubble1(copy.deepcopy(unsorted_list)))
        bubble2_res.append(bubble2(copy.deepcopy(unsorted_list)))
        bubble3_res.append(bubble3(copy.deepcopy(unsorted_list)))
        bubble4_res.append(bubble4(copy.deepcopy(unsorted_list)))
        insert_res.append(insert_sort(copy.deepcopy(unsorted_list)))
        select_res.append(select_sort(copy.deepcopy(unsorted_list)))
        quick_res.append(quick(copy.deepcopy(unsorted_list)))


    plt.plot(lists_lens, bubble1_res, label='bubbleV1', color='blue')
    plt.plot(lists_lens, bubble2_res, label='bubbleV2', color='red')
    plt.plot(lists_lens, bubble3_res, label='bubbleV3', color='yellow')
    plt.plot(lists_lens, bubble4_res, label='bubbleV4', color='green')
    plt.plot(lists_lens, insert_res, label='insert', color='purple')
    plt.plot(lists_lens, select_res, label='select', color='orange')
    plt.plot(lists_lens, quick_res, label='quick', color='black')

    plt.legend()
    plt.show()

#measure_sorts()


def measure_t():
    n = [random.randint(0,100) for i in range (100000)]

    t_start = time.time()
    vystup_bubble1 = bubble1(copy.deepcopy(n))
    t_end = time.time()
    bubble1_time = t_end - t_start

    print(vystup_bubble1)
    print(f"Cas bubble1: {bubble1_time:.6f} s")


    t2_start = time.time()
    vystup_bubble2 = bubble2(copy.deepcopy(n))
    t2_end = time.time()
    bubble2_time = t2_end - t2_start

    print(vystup_bubble2)
    print(f"Cas bubble2: {bubble2_time:.6f} s")


    t3_start = time.time()
    vystup_bubble3 = bubble3(copy.deepcopy(n))
    t3_end = time.time()
    bubble3_time = t3_end - t3_start

    print(vystup_bubble3)
    print(f"Cas bubble3: {bubble3_time:.6f} s")


    t4_start = time.time()
    vystup_bubble4 = bubble4(copy.deepcopy(n))
    t4_end = time.time()
    bubble4_time = t4_end - t4_start

    print(vystup_bubble4)
    print(f"Cas bubble4: {bubble4_time:.6f} s")


    t5_start = time.time()
    vystup_insert = insert_sort(copy.deepcopy(n))
    t5_end = time.time()
    insert_time = t5_end - t5_start

    print(vystup_insert)
    print(f"Cas insert: {insert_time:.6f} s")


    t6_start = time.time()
    vystup_select = select_sort(copy.deepcopy(n))
    t6_end = time.time()
    select_time = t6_end - t6_start

    print(vystup_select)
    print(f"Cas select: {select_time:.6f} s")


    t7_start = time.time()
    vystup_quick = quick(copy.deepcopy(n))
    t7_end = time.time()
    quick_time = t7_end - t7_start

    print(vystup_quick)
    print(f"Cas quick: {quick_time:.6f} s")

measure_t()