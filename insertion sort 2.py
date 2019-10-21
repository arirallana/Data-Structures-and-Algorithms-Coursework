'''
Implementation of insertion sort algorithm to sort list of integers. 
'''

def insertion_sort_2(list_):
    for i in range(1, len(list_)):
        temp = list_[i]
        j = i-1
        while j>=0 and list_[j]>temp:
            list_[j+1], list_[j] = list_[j], list_[j+1]
            j -=1
        list_[j+1] = temp
    print(list_)
    return(list_)

list_ = [7, -5, 2, 16, 4]
insertion_sort_2(list_)
