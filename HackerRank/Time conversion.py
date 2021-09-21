#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    converted = s.split(':')
    
    if s[-2:] == 'AM':
        if converted[0] == '12':
            converted[0] = '00'      
        
    elif s[-2:] == 'PM':
        if converted[0] != '12':
            converted[0] = str(int(converted[0]) + 12)
            
    converted_s = ':'.join([str(item) for item in converted])
    return(converted_s[:-2])
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
