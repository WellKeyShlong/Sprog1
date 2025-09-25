import time
import random
import copy

import matplotlib.pyplot as plt

from bubble1 import bubble1
from bubble2 import bubble2
from bubble3 import bubble3
from bubble4 import bubble4


def measure_sorts():
    lists_lens = [n for n in range (10,50,10)]

    bubble1_res = []
    bubble2_res = []
    bubble3_res = []
    bubble4_res = []

    for n in range(10,50,10):
        unsorted_list = [random.randint(0,n**2) for i in range (n)]

        bubble1_res.append(bubble1(copy.deepcopy(unsorted_list)))
        bubble2_res.append(bubble2(copy.deepcopy(unsorted_list)))
        bubble3_res.append(bubble3(copy.deepcopy(unsorted_list)))
        bubble4_res.append(bubble4(copy.deepcopy(unsorted_list)))
    
    plt.plot(lists_lens, bubble1_res, label='bubbleV1', color='blue')
    plt.plot(lists_lens, bubble2_res, label='bubbleV2', color='red')
    plt.plot(lists_lens, bubble3_res, label='bubbleV3', color='yellow')
    plt.plot(lists_lens, bubble4_res, label='bubbleV4', color='green')

    plt.legend()
    plt.show()

measure_sorts()