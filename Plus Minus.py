#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    
    positives = 0
    zeroes = 0
    negatives = 0
    
    for i in range(len(arr)):
        if arr[i] > 0:
            positives += 1
        elif arr[i] == 0:
            zeroes += 1
        else:
            negatives += 1
        
    positive_ratio = round(positives / len(arr), 6)
    zero_ratio = round(zeroes / len(arr), 6)
    negative_ratio = round(negatives / len(arr), 6)
        
    print(positive_ratio)
    print(negative_ratio)
    print(zero_ratio)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
