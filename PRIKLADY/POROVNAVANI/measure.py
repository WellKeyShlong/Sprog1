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
#from merge import merge_sort

def measure_sorts():
    lists_lens = [n for n in range (10,200,10)]

    bubble1_res = []
    bubble2_res = []
    bubble3_res = []
    bubble4_res = []
    insert_res = []
    select_res = []
    quick_res = []
    #merge_res = []

    for n in range(10,200,10):
        unsorted_list = [random.randint(0,n**2) for i in range (n)]

        bubble1_res.append(bubble1(copy.deepcopy(unsorted_list)))
        bubble2_res.append(bubble2(copy.deepcopy(unsorted_list)))
        bubble3_res.append(bubble3(copy.deepcopy(unsorted_list)))
        bubble4_res.append(bubble4(copy.deepcopy(unsorted_list)))
        insert_res.append(insert_sort(copy.deepcopy(unsorted_list)))
        select_res.append(select_sort(copy.deepcopy(unsorted_list)))
        quick_res.append(quick(copy.deepcopy(unsorted_list)))
        #merge_res.append(quick(copy.deepcopy(unsorted_list)))


    plt.plot(lists_lens, bubble1_res, label='bubbleV1', color='blue')
    plt.plot(lists_lens, bubble2_res, label='bubbleV2', color='red')
    plt.plot(lists_lens, bubble3_res, label='bubbleV3', color='yellow')
    plt.plot(lists_lens, bubble4_res, label='bubbleV4', color='green')
    plt.plot(lists_lens, insert_res, label='insert', color='purple')
    plt.plot(lists_lens, select_res, label='select', color='orange')
    plt.plot(lists_lens, quick_res, label='quick', color='black')
    #plt.plot(lists_lens, merge_res, label='merge', color='pink')

    plt.legend()
    plt.show()

measure_sorts()