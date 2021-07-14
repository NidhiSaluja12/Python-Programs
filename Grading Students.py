#!/bin/python3

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    result = []
    for grade in grades:
        multiple = ((grade//5)*5)+5
        if grade >= 38:
            if multiple-grade < 3:
                result.append(multiple)
            else:
                result.append(grade)
        else:
            result.append(grade)
            
    return result
          
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

