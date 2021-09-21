#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    
    cipher_text = ''
    
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                cipher_text = cipher_text + chr((ord(s[i]) + k - ord('a')) % 26 + ord('a'))
                i += 1
            else:
                cipher_text = cipher_text + chr((ord(s[i]) + k - ord('A')) % 26 + ord('A'))
                i += 1
        
        else:
            cipher_text = cipher_text + s[i]
            i += 1
    return cipher_text

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
