#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    
    num_sums = []
    
    for i in range(len(arr)):
        num_sums.append(sum(arr) - arr[i])
        i += 1
    print(min(num_sums), max(num_sums))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
