'''
Implementation of the linear search algorithm
'''

def linear_search(list_, val):
    for i in range(len(list_)+1):
        if list_[i] == val:
            print(list_.index(val))
            return list_.index(val)

list_ = [1,2,3,6,56,32]
linear_search(list_, 32)


'''
Best case: the value is found at the first index
worst case: the value is found at the last index
runtime = n
'''
