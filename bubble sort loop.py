'''
Implementation of bubble sort algorith to sort numbers in a list in ascending 'a' or descending 'd' order. 
'''

def bubble_sort(l,t='a'):
    n = len(l)-1
    while n != 0:
        for i in range(n):
            if (l[i] < l[i+1] if t =='d' else l[i] > l[i+1]):
                l[i], l[i+1] = l[i+1], l[i]
        n-=1
    print(l)
    return l

a = [10, 5 ,20, 3, 35]

bubble_sort(a)

