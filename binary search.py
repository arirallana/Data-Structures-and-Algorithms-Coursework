'''
This is the implementation of the binary search algorith to return the index of a search number from a list.
'''

import math

def binary_search(list_, val):
    low = 0
    high = len(list_)-1
    while low<=high:
        mid = math.floor((low + high)/2)
        if val==list_[mid]:
            print(list_.index(val))
            return True
        elif val<list_[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

list_ = [1,5,4,6,8,10]
binary_search(list_, 6)
